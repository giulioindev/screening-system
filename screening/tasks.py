from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from uuid import UUID

from django.db.utils import DatabaseError

from celery import shared_task
from screening.models import Candidate
from screening.typing import CandidateData, ScreeningLog
from screening.utils import send_to_azure

if TYPE_CHECKING:
    from uuid import UUID

    from celery import Task

logger = logging.getLogger(__name__)


@shared_task(bind=True)
def run_screening(self: Task, candidate_id: UUID):
    """Run screening for a candidate.

    Args:
        self (Task): The task instance.
        candidate_id (UUID): The ID of the candidate to run screening for.
    """
    try:
        candidate = Candidate.objects.get(id=candidate_id)
        is_duplicate = Candidate.objects.filter(email=candidate.email).count() > 1
        screening_log = ScreeningLog(
            is_email_format_valid=True,  # NOTE: This is a placeholder.
            is_duplicate=is_duplicate,
            is_blacklisted=False,  # NOTE: This is a placeholder.
        )
        candidate.status = Candidate.Status.REJECTED if is_duplicate else Candidate.Status.CHECKED
        candidate.screening_log = screening_log
        candidate.save()
        send_to_azure(CandidateData(candidate_id=candidate.id, status=candidate.status, screening_result=screening_log))
    except (Candidate.DoesNotExist, DatabaseError) as error:
        logger.error("Error running screening for candidate %s: %s", candidate_id, error)
        self.retry(exc=error, max_retries=3)
