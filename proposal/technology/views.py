from rest_framework import viewsets
from .models import TechnologyStack, Technology

from .serializers import TechnologyStackSerializer, TechnologyStackCreateSerializer, TechnologySerializer

class TechnologyStackViewSet(viewsets.ModelViewSet):
    queryset = TechnologyStack.objects.all()
    serializer_class = TechnologyStackSerializer  

    def get_serializer_class(self):
        if self.action == 'create':
            return TechnologyStackCreateSerializer  # Use restricted fields for creation
        return super().get_serializer_class()
    
    
    
class TechnologyViewSet(viewsets.ModelViewSet):
    
    
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
