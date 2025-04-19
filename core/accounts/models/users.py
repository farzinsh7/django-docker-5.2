from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from ..managers import UserManager
from ..validators import iranian_phone_number_validator


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model by AbstractBaseUser
    """

    
    phone_number = models.CharField(
        max_length=15, validators=[iranian_phone_number_validator], unique=True
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone_number
