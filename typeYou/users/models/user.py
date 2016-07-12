from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseUser(AbstractUser):

    follower_set = models.ManyToManyField(
            'self',
            symmetrical=False,
            related_name='following_set',
            through='Follow',
            through_fields=('following', 'follower'),
    )

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
    class Meta:
        permissions = (
                ('is_student', 'user is a student'),
        )
