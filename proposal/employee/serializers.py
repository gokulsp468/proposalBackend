from rest_framework import serializers
from .models import Employee
from designationApp.models import Designation
from technology.models import Technology



class EmployeeSerializer(serializers.ModelSerializer):
    designation = serializers.PrimaryKeyRelatedField(
        queryset = Designation.objects.all(),
        
    )
    
    technologies = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset = Technology.objects.all(),
        
        
    )
    
    photo = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    
    class Meta:
        model = Employee
        fields = ['id', 'empId', 'firstName', 'lastName', 'phoneNumber', 'email', 'photo', 'designation', 'technologies']
        
    def create(self, validated_data):
        technologies = validated_data.pop('technologies', [])
        employee = Employee.objects.create(**validated_data)
        employee.technologies.set(technologies)
        return employee

    def update(self, instance, validated_data):
        technologies = validated_data.pop('technologies', None)
        instance = super().update(instance, validated_data)
        
        if technologies is not None:
            instance.technologies.set(technologies)
        
        return instance