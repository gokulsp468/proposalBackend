from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from technology.models import TechnologyStack, Technology
from .serializers import TechnologyStackSerializer ,TechnologyEmployeeSerializer, ProjectSerializer
from drf_yasg.utils import swagger_auto_schema


class TechnologyStackList(APIView):
    def get(self, request, format=None):
        technologystacks = TechnologyStack.objects.all()
        serializer = TechnologyStackSerializer(technologystacks, many=True)
        return Response(serializer.data)
    
    
    
class TechnologyEmployeeListView(APIView):
    def get(self, request, format=None):
        technologies = Technology.objects.all()
        serializer = TechnologyEmployeeSerializer(technologies, many=True)
        return Response(serializer.data)
    
    
    
    
class ProjectCreateAPIView(APIView):
    @swagger_auto_schema(request_body=ProjectSerializer)
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)