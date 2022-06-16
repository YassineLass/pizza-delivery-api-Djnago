from enum import unique
import imp
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# from django.contrib.auth.base_user import BaseUserManager   
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class CustomUserManager(BaseUserManager):

    def create_user(self,username,email,password,**extra_fields):
        if not email:
            raise ValueError(("No email found "))
        if not username:
            raise ValueError(("No username found "))
        self.normalize_email(email)
        new_user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields)
        new_user.set_password(password)
        new_user.save()
        return new_user

    def create_superuser(self,username,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if(extra_fields.get('is_staff') is not True):
            raise ValueError(("Supperuser should have is_staff set to True"))
        if(extra_fields.get('is_superuser') is not True):
            raise ValueError(("Supperuser should have is_superuser set to True"))       
        return self.creat_user(username=username, email=email,password=password,**extra_fields)
        
class User(AbstractUser):
    username = models.CharField(max_length=25,unique=True)
    email = models.EmailField(max_length=50,unique=True)
    phone_number = PhoneNumberField(null=False,unique=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.email

 