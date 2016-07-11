from django.db import models
from users.models import Teacher


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

    user = models.ForeignKey(Teacher)

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
