from django.db import models
import uuid

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    is_registered = models.BooleanField(default=True)
    user_type = models.CharField(max_length=50,default='client')
    created_at = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to='client_image/')

    def __str__(self):
        return self.name

