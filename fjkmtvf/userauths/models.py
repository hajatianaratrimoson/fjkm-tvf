from django.db import models
from django.contrib.auth.models import AbstractUser

"""This is an extended User model using email for authentification. 

Returns:
    _type_: User Model
"""
class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    
    bio = models.CharField(max_length=100)
    
    # Force email authentification using django admin username 20/01.2025
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username
