from django.db import models

from users.models import BaseUser
from quizzes.models import Question


class AnswerManager(models.Manager):

    def public(self):
        return self.filter(is_public=True)


class Answer(models.Model):

    objects = AnswerManager()

    user = models.ForeignKey(BaseUser)

    question = models.ForeignKey(Question)

    ans = models.CharField(
        max_length=64,
    )

    correct = models.NullBooleanField(
        blank=True,
        null=True,
        default=None,
    )

    is_public = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "by " + self.user.username
