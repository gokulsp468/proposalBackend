from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DesignationViewSet

router = DefaultRouter()
router.register(r'designations', DesignationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
