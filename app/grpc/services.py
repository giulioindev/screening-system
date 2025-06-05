from django_grpc_framework import generics

from app.grpc.serializers import CandidateProtoSerializer
from screening.models import Candidate


class CandidateStatusService(generics.GenericService):
    """Candidate status service."""

    queryset = Candidate.objects.all()
    serializer_class = CandidateProtoSerializer
    lookup_field = "id"
    lookup_request_field = "id"

    def GetCandidateStatus(self, request, context):
        """Get candidate status.

        Args:
            request: gRPC request.
            context: gRPC context.

        Returns:
            CandidateProtoSerializer: Candidate status.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return serializer.message
