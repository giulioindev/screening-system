from typing import TypedDict
from uuid import UUID


class ScreeningLog(TypedDict):
    """Screening log for a candidate."""

    is_email_format_valid: bool
    is_duplicate: bool
    is_blacklisted: bool


class CandidateData(TypedDict):
    """Candidate data."""

    candidate_id: UUID
    status: str
    screening_result: ScreeningLog
