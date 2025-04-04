from django.db import models
from django.contrib.auth.models import AbstractUser

"""This is an extended User model using email for authentification. 

Returns:
    _type_: User Model
"""
class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Mailaka")
    username = models.CharField(max_length=100, verbose_name="Fiantso")
    
    bio = models.CharField(max_length=100, verbose_name="Fanamarihana")
    
    avatar = models.ImageField(upload_to='profile')
    
    # Force email authentification using django admin username 20/01.2025
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
    
    #Force all new user to have the same default password
    password = models.CharField(verbose_name="Mot de pass", max_length=200, default="pbkdf2_sha256$600000$tvf$c3Y/SMHxhbwc0eRo1LGjNOHPR+eSdelnupX6zRChMZE=")
    
    def __str__(self):
        return self.username
