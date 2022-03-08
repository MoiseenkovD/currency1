import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    email = models.EmailField('email address', blank=True, unique=True)

    # def save(self, *args, **kwargs):
    #     if not self.username:
    #         self.username = str(uuid.uuid4())
    #
    #     super().save(*args, **kwargs)
