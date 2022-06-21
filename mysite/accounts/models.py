from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    # username = models.CharField(max_length=200,unique=True, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg",upload_to='user')
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.name
    
