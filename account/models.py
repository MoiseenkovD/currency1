import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    email = models.EmailField('email address', blank=True, unique=True)
