from enum import unique
import imp
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager   
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class CustomUserManager(BaseUserManager):

    def creat_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(("No email found "))
        self.normalize_email(email)
        new_user = self.model(email,**extra_fields)
        new_user.setpassword(password)
        new_user.save()
        return new_user

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if(extra_fields.get('is_staff') is not True):
            raise ValueError(("Supperuser should have is_staff set to True"))
        if(extra_fields.get('is_superuser') is not True):
            raise ValueError(("Supperuser should have is_superuser set to True"))       
        return self.creat_user(email,password,**extra_fields)

class User(AbstractUser):
    username = models.CharField(max_length=25,unique=True)
    email = models.EmailField(max_length=50,unique=True)
    phone_number = PhoneNumberField(null=False,unique=True)

    def __str__(self):
        return f"<User {self.email} "

 