from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from .manager import custommanager

# Create your models here.
class student_custom(AbstractUser,PermissionsMixin):
    username=models.CharField( max_length=50)
    firstname=models.CharField( max_length=50)
    lastname=models.CharField( max_length=50)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    Role=models.CharField(max_length=50,null=True)

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []

    objects = custommanager()

    def __str__(self):
        return self.email

class application_model(models.Model):
    application_id=models.CharField(max_length=20)
    university_name=models.CharField(max_length=20)
    program_name=models.CharField(max_length=20)
    study_mode=models.CharField(max_length=20)
    customer=models.CharField(max_length=20)
    email=models.EmailField(null=True)
    status=models.CharField(max_length=20,null=True)
