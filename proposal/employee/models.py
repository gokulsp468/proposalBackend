from django.db import models
import uuid
from designationApp.models import Designation
from technology.models import Technology

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    empId = models.CharField(max_length=20, unique=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    isActive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    photo = models.ImageField(upload_to='employee_images/', null=True, blank=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, related_name='employees')
    technologies = models.ManyToManyField(Technology, related_name='employees', blank=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
