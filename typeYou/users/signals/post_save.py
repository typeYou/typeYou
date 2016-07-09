from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission

from users.models import Teacher, Student
from notifications.models import SMSNotification


@receiver(post_save, sender=Teacher)
def post_save_teacher(sender, instance, created, **kwargs):
    if created:
        permission = Permission.objects.get(codename='is_teacher')
        permission1 = Permission.objects.get(codename='create_question')
        instance.user_permissions.add(
                permission,
                permission1,
        )
        sms = SMSNotification.objects.create(
                sender='01031186228',
                receiver=instance.phonenumber,
                content='Thank you for registering as a Teacher',
        )
        instance.save()


@receiver(post_save, sender=Student)
def post_save_student(sender, instance, created, **kwargs):
    if created:
        permission = Permission.objects.get(codename='is_student')
        instance.user_permissions.add(
                permission,
        )
        sms = SMSNotification.objects.create(
                sender='01031186228',
                receiver=instance.phonenumber,
                content='Thank you for registering as a Student',
        )
        instance.save()
