from rest_framework import viewsets
from .models import Template
from .serializers import TemplateSerializer, TemplateCreateSerializer

class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer  

    def get_serializer_class(self):
        if self.action == 'create':
            return TemplateCreateSerializer  # Use restricted fields for creation
        return super().get_serializer_class()
