from django.dispatch import receiver
from django.db.models.signals import post_save

from notifications.models import SMSNotification


@receiver(post_save, sender=SMSNotification)
def post_save_notification(sender, instance, created, **kwargs):
    if created:
        instance.send_notification()
