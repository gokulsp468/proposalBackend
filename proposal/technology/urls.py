
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TechnologyStackViewSet, TechnologyViewSet

router = DefaultRouter()
router.register(r'technology-stacks', TechnologyStackViewSet)
router.register(r'technologies', TechnologyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
