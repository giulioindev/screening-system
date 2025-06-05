from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import SimpleRouter

from screening.v1.views import CandidateViewSet

router = SimpleRouter()
router.register("candidates", CandidateViewSet, basename="candidate")

urlpatterns = [
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema-v1", authentication_classes=[], permission_classes=[]),
        name="swagger-ui",
    ),
    path(
        "schema/",
        SpectacularAPIView.as_view(api_version="v1", authentication_classes=[], permission_classes=[]),
        name="schema-v1",
    ),
    *router.urls,
]
