from hashids import Hashids

from django.db.models.signals import post_save
from django.dispatch import receiver

from quizzes.models import Quiz


@receiver(post_save, sender=Quiz)
def post_save_quiz(sender, instance, created, **kwargs):
    if created:
        hashids = Hashids(salt="post_save_quiz", min_length=4)
        instance.hash_id = hashids.encode(instance.id)
        instance.save()
