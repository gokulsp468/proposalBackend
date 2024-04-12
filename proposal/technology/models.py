from django.db import models
import uuid

class TechnologyStack(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    technology_stack = models.CharField(max_length=255)
    alias = models.CharField(max_length=50)
    order = models.PositiveIntegerField()
    project_count = models.PositiveIntegerField(default=0)
    technology_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.technology_stack



class Technology(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    technology_stack = models.ForeignKey('TechnologyStack', on_delete=models.CASCADE, related_name='technologies')
    technology_name = models.CharField(max_length=255)
    label = models.CharField(max_length=255, blank=True)  
    project_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.label = self.technology_name  
        super(Technology, self).save(*args, **kwargs)

    def __str__(self):
        return self.technology_name
