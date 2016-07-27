from django.core.urlresolvers import reverse
from django.db import models

from users.models import BaseUser


class QuestionManager(models.Manager):

    def public(self):
        return self.filter(is_public=True)


class Question(models.Model):

    objects = QuestionManager()

    user = models.ForeignKey(BaseUser)

    quiz = models.ForeignKey("Quiz")

    title = models.CharField(
        max_length=256,
    )

    ans1 = models.CharField(
        max_length=64,
    )
    ans2 = models.CharField(
        max_length=64,
    )
    ans3 = models.CharField(
        max_length=64,
    )
    ans4 = models.CharField(
        max_length=64,
    )

    correct_ans = models.CharField(
            max_length=64,
            blank=True,
            null=True,
    )

    is_public = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("quizzes:quiz_edit", kwargs={
            "slug": self.quiz.hash_id,
        })

    def get_ans(self, index):
        if index == 1:
            return self.ans1
        elif index == 2:
            return self.ans2
        elif index == 3:
            return self.ans3
        elif index == 4:
            return self.ans4
        else:
            return None
