from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager()
    pass
    

class UserProfile(AbstractBaseUser, PermissionsMixin)
    email = models.EmailField(max_length=255, unique=True)
    name= models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    
