from django.db import models

from users.models import BaseUser
from quizzes.models import Quiz


class Solve(models.Model):

    user = models.ForeignKey(BaseUser)
    quiz = models.ForeignKey(Quiz)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
