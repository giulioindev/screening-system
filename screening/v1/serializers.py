from rest_framework import serializers

from screening.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    """Candidate serializer."""

    class Meta:
        model = Candidate
        read_only_fields = ["id", "status", "screening_log", "created_at", "updated_at"]
        fields = [*read_only_fields, "full_name", "email"]
