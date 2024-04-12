import json
from django.core.exceptions import ValidationError
from .models import Designation, Permission
from rest_framework import serializers
from django.core.exceptions import ValidationError


class DesignationSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(
        queryset=Permission.objects.all(),
        many=True,
        allow_empty=False
    )

    class Meta:
        model = Designation
        fields = ['id', 'name', 'description', 'permissions']

    def validate_permissions(self, value):
        if not value:
            raise serializers.ValidationError("At least one permission is required.")
        permission_ids = {perm.id for perm in value}

        for perm in value:
            if perm.requires:
                corrected_json_string = perm.requires.replace("'", '"')
                try:
                    requires_list = json.loads(corrected_json_string)  # Load the JSON data into a list
                except json.JSONDecodeError:
                    raise ValidationError(f"Invalid JSON format in requires field for permission {perm.permission_label}")

                for required_group in requires_list:
                    # Handle OR conditions within a group of required permissions
                    required_pids = required_group.split('|')
                    required_perms = Permission.objects.filter(pid__in=required_pids)
                    required_ids = {req.id for req in required_perms}

                    if not required_ids & permission_ids:  # Check for intersection
                        missing_labels = ", ".join(required_pids)
                        raise ValidationError(
                            f"The permission '{perm.permission_label}' requires at least one of the following permissions which are not included: {missing_labels}"
                        )
        return value
