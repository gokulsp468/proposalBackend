from django.db import models
import uuid

class Module(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='submodules', null=True, blank=True)
    module = models.CharField(max_length=255)
    module_label = models.CharField(max_length=255)
    order = models.FloatField()
    app_visibility = models.BooleanField(default=True)
    web_visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.module

class Permission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='permissions')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_permissions', null=True, blank=True)
    permission = models.CharField(max_length=255)
    permission_label = models.CharField(max_length=255)
    pid = models.CharField(max_length=255)
    requires = models.CharField(max_length=255, null=True, blank=True)
    optional_with = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.permission

