from django.urls import path
from .views import PermissionListView


urlpatterns = [
    path('permission_list', PermissionListView.as_view(), name='permission_list'),
]
