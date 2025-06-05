import uuid
from enum import unique

from django.db import models


class Candidate(models.Model):
    """Candidate model."""

    @unique
    class Status(models.TextChoices):
        """Candidate status choices."""

        PENDING = "pending", "Pending"
        CHECKED = "checked", "Checked"
        REJECTED = "rejected", "Rejected"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    status = models.CharField(max_length=255, choices=Status.choices, default=Status.PENDING)
    screening_log = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self) -> str:
        """Return the candidate's full name.

        Returns:
            str: The candidate's full name.
        """
        return f"Candidate {self.full_name}"
