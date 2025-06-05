from django_grpc_framework import proto_serializers

from app.grpc import candidate_pb2
from screening.models import Candidate


class CandidateProtoSerializer(proto_serializers.ModelProtoSerializer):
    """Candidate proto serializer."""

    class Meta:
        model = Candidate
        read_only_fields = ["status", "screening_log"]
        fields = [*read_only_fields]
        proto_class = candidate_pb2.Candidate
