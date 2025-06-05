import logging

from screening.typing import CandidateData

logger = logging.getLogger(__name__)


def send_to_azure(candidate_data: CandidateData):
    """Send candidate data to Azure.

    Args:
        candidate_data (CandidateData): The candidate data to send to Azure.
    """
    logger.info("Sending candidate data to Azure: %s", candidate_data)
