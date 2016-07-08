from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission

from users.models import Teacher


@receiver(post_save, sender=Teacher)
def post_save_teacher(sender, instance, created, **kwargs):
    if created:
        permission = Permission.objects.get(codename='is_teacher')
        permission1 = Permission.objects.get(codename='create_question')
        instance.user_permissions.add(
                permission,
                permission1,
        )
        instance.save()
