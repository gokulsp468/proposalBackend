from rest_framework import serializers
from .models import Template
from client.models import Client
from client.serializers import ClientSerializer
    
    
class TemplateSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    logo = serializers.ImageField(required=False)
    banner = serializers.ImageField(required=False)
    back_cover = serializers.ImageField(required=False)
    back_cover_logo = serializers.ImageField(required=False)

    class Meta:
        model = Template
        fields = ['id', 'title', 'logo', 'banner', 'back_cover', 'back_cover_logo', 'preview_url', 'footer', 'footer_link', 
                  'introduction', 'companyName', 'email', 'name', 'phone', 'address', 'description', 'is_default',
                   'created_at', 'client']
        read_only_fields = ['id', 'created_at']
        
        
class TemplateCreateSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset = Client.objects.all(),
        
    )
    logo = serializers.ImageField(required=False)
    banner = serializers.ImageField(required=False)
    back_cover = serializers.ImageField(required=False)
    back_cover_logo = serializers.ImageField(required=False)

    class Meta:
        model = Template
        fields = ['id', 'title', 'logo', 'banner', 'back_cover', 'back_cover_logo', 'footer', 
                  'introduction', 'companyName', 'email', 'name', 'phone', 'address', 'description', 'is_default',
                    'client']
        read_only_fields = ['id']