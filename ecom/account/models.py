from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from .manager import UserManager

# Custom User Model
class CustomUser(AbstractUser):
    username = None  # Remove the default username field
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    profile_image = models.ImageField(upload_to='profile_image',  null=False)

    USERNAME_FIELD = 'email'  # Use email as the unique identifier
    REQUIRED_FIELDS = ['phone_number']  # Additional fields required for superuser creation

    objects = UserManager()

    def __str__(self):
        return self.email
