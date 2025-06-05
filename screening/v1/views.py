from __future__ import annotations

from typing import TYPE_CHECKING, Any

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from screening.models import Candidate
from screening.tasks import run_screening
from screening.v1.serializers import CandidateSerializer

if TYPE_CHECKING:
    from rest_framework.request import Request
    from rest_framework.response import Response


class CandidateViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """Candidate view set."""

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Create a candidate and run screening.

        Args:
            request (Request): The request object.
            args (Any): The positional arguments.
            kwargs (Any): The keyword arguments.

        Returns:
            Response: The response object.
        """
        response = super().create(request, *args, **kwargs)
        run_screening.delay(response.data["id"])
        return response
