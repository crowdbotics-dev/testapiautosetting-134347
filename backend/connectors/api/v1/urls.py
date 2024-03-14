from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134347ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134347", Testconnectors134347ViewSet, basename="testconnectors134347"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
