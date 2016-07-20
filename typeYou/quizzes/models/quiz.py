from django.core.urlresolvers import reverse

from django.db import models
from users.models import BaseUser


class QuizManager(models.Manager):

    def public(self):
        return self.filter(is_public=True)

    def published(self):
        return self.filter(is_published=True)


class Quiz(models.Model):

    objects = QuizManager()

    hash_id = models.CharField(
        max_length=4,
        blank=True,
        null=True,
    )

    user = models.ForeignKey(BaseUser)

    solve_user_set = models.ManyToManyField(
        BaseUser,
        related_name="solve_quiz_set",
        through="Solve",
    )

    is_published = models.BooleanField(
        default=False,
    )

    is_public = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hash_id

    def get_absolute_url(self):
        return reverse("quizzes:quiz_detail", kwargs={
            "slug": self.hash_id,
        })

    def get_create_action_url(self):
        return reverse("quizzes:question_create", kwargs={
            "slug": self.hash_id,
        })
