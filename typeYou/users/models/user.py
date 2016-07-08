from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseUser(AbstractUser):
    phonenumber = models.CharField(
            max_length=16,
    )
