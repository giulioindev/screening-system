from django.contrib import admin

from screening.models import Candidate


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    """Candidate admin."""

    list_display = ("full_name", "email", "status", "created_at", "updated_at")
    list_filter = ("status",)
    search_fields = ("full_name", "email")
