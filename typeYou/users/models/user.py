from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseUser(AbstractUser):
    phonenumber = models.CharField(
            max_length=16,
    )


class Teacher(BaseUser):
    class Meta:
        permissions = (
                ('is_teacher', 'user is a teacher'),
                ('create_question', 'user can create question'),
        )


class Student(BaseUser):
    pass
