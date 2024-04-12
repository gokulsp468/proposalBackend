from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Module
from .serializers import ModuleSerializer

class PermissionListView(APIView):
    def get(self, request, format=None):
        modules = Module.objects.filter(parent__isnull=True)
        serializer = ModuleSerializer(modules, many=True)
        return Response(serializer.data)
