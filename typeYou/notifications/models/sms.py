from django.db import models

from .base import BaseNotification


class SMSNotification(BaseNotification):

    class Meta:
        verbose_name = 'SMS Notification'
        verbose_name_plural = 'SMS Notification'

    def send_notification(self):
        from notifications.tasks import SendSMSTask
        sms = SendSMSTask()
        sms.run(self.id)
