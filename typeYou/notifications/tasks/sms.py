import os

from notifications.models import SMSNotification
from .base import SendNotificationBaseTask


class SendSMSTask(SendNotificationBaseTask):

    def get_object(self, object_id):
        sms = SMSNotification.objects.get(id=object_id)
        return sms

    def get_api_base_url(self):
        api_base_url = os.environ.get('SMS_BASE_URL')
        return api_base_url

    def get_headers(self):
        headers = {
                os.environ.get('SMS_HEADERS1'): os.environ.get('SMS_HEADERS2'),
        }
        return headers

    def get_data(self, object):
        data = {
            'send_phone': object.sender,
            'dest_phone': object.receiver,
            'msg_body': object.content,
        }
        return data
