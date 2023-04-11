from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from user.manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICE = [
        ['ADMIN', 'ADMIN'],
        ['RECTOR', 'RECTOR'],
        ['DEAN', 'DEAN'],
        ['DEPUTY_DEAN', 'DEPUTY_DEAN'],
        ['TEACHER', 'TEACHER'],
        ['MANAGER', 'MANAGER'],
        ['STUDENT', 'STUDENT'],
        ['PARENT', 'PARENT'],
    ]

    USER_ID = models.CharField(max_length=150, unique=True)
    ROLE = models.CharField(max_length=15, choices=ROLE_CHOICE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "USER_ID"

    class Meta:
        db_table = 'user'

