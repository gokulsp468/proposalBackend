from rest_framework import serializers
from technology.models import TechnologyStack, Technology
from employee.models import Employee
from .models import Project

class TechnologySerializer(serializers.ModelSerializer):
    technologyStackId = serializers.UUIDField(source='technology_stack.id', read_only=True)

    class Meta:
        model = Technology
        fields = ('id', 'technologyStackId', 'technology_name', 'label')

class TechnologyStackSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)
    technologyStack = serializers.CharField(source='technology_stack', read_only=True)
    alias = serializers.CharField(read_only=True)

    class Meta:
        model = TechnologyStack
        fields = ('id', 'technologyStack', 'alias', 'technologies')



class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = ['id', 'firstName', 'lastName', 'photo']
        
        
        
class TechnologyEmployeeSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    technologyId = serializers.UUIDField(source='id', read_only=True)

    class Meta:
        model = Technology
        fields = ['technologyId', 'technology_name', 'users']

    def get_users(self, obj):
        employees = obj.employees.all()
        return EmployeeSerializer(employees, many=True).data
    
    
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'client_id', 'project_name', 'project_type', 'platform',
            'template_id', 'emails', 'hourly_rate', 'executive_summary',
            'scope_of_work', 'deliverables', 'queries_assumption',
            'technology_allocation', 'other_resources', 'qa_percentage',
            'reference', 'reference_documents'
        ]

    def create(self, validated_data):
        # You can add custom creation logic here
        return Project.objects.create(**validated_data)