from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    status = models.BooleanField(default=False)
    creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title