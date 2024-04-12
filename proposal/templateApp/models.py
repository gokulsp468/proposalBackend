from django.db import models
from client.models import Client
import uuid

class Template(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, blank=True)
    logo = models.ImageField(upload_to='templates/logos/', blank=True)
    banner = models.ImageField(upload_to='templates/banners/', blank=True)
    back_cover = models.ImageField(upload_to='templates/back_covers/', blank=True)
    back_cover_logo = models.ImageField(upload_to='templates/back_cover_logos/', blank=True)
    preview_url = models.URLField(max_length=1024, blank=True)  # Retain as URLField for non-image link
    footer = models.TextField(blank=True)
    footer_link = models.URLField(max_length=1024, blank=True,null=True)
    introduction = models.TextField(blank=True)
    companyName = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)
    description = models.TextField(blank=True)
    is_default = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='templates')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # First save to get the instance with an ID
        if not self.preview_url:
            self.preview_url = self.get_preview_url()
            super().save(update_fields=['preview_url'])

    def get_preview_url(self):
        # Assuming you have named your URL in urls.py
        return f"http://127.0.0.1:8000/api/template/templates/{self.id}"

    def __str__(self):
        return self.title
