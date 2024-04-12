from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer, ClientCreateSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer  

    def get_serializer_class(self):
        if self.action == 'create':
            return ClientCreateSerializer  # Use restricted fields for creation
        return super().get_serializer_class()
