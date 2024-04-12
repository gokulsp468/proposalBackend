from django.urls import path
from .views import TechnologyStackList, TechnologyEmployeeListView, ProjectCreateAPIView
urlpatterns = [
    path('technology/', TechnologyStackList.as_view()),
     path('technology/users/', TechnologyEmployeeListView.as_view()),
     path('proposals/', ProjectCreateAPIView.as_view()),
]
