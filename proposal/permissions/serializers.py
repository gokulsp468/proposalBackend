from rest_framework import serializers
from .models import Module, Permission

class RecursivePermissionSerializer(serializers.Serializer):
    def to_representation(self, value):
        # This serializer will be used for recursive permissions (sub-permissions)
        serializer = PermissionSerializer(value, context=self.context)
        return serializer.data

class PermissionSerializer(serializers.ModelSerializer):
    sub_permissions = RecursivePermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Permission
        fields = ('id', 'permission', 'permission_label', 'pid', 'sub_permissions', 'optional_with', 'requires')

class ModuleSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()
    submodules = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = ('id', 'module', 'module_label', 'order', 'app_visibility', 'web_visibility', 'permissions', 'submodules')

    def get_permissions(self, obj):
    # Filter out permissions that are designated as sub-permissions
        top_level_permissions = obj.permissions.filter(parent__isnull=True)
        return PermissionSerializer(top_level_permissions, many=True).data


    def get_submodules(self, obj):
        submodules = obj.submodules.all()
        return ModuleSerializer(submodules, many=True).data
