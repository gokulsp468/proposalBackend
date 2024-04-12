from rest_framework import viewsets
from rest_framework import permissions
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard CRUD actions for Employee model.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
   

    def perform_create(self, serializer):
        
        serializer.save()

    def perform_update(self, serializer):
        
        serializer.save()
