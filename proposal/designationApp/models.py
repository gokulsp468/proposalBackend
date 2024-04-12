from django.db import models
from permissions.models import Permission
import uuid


class Designation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=50, blank = True)
    permissions = models.ManyToManyField(Permission, related_name='designations')

    def __str__(self):
        return self.name
