from rest_framework import serializers
from .models import TechnologyStack, Technology

class TechnologyStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyStack
        fields = '__all__'  # This serializer shows all fields

class TechnologyStackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyStack
        fields = ['technology_stack', 'alias', 'order'] 



class TechnologySerializer(serializers.ModelSerializer):
    technology_stack = TechnologyStackSerializer()  # Nesting the full TechnologyStackSerializer here

    class Meta:
        model = Technology
        fields = ['id', 'technology_stack', 'technology_name', 'label', 'project_count']

    def validate(self, data):
        
        if 'label' in data and data.get('label') != data.get('technology_name'):
            raise serializers.ValidationError("Label must be the same as technology name.")
        return data