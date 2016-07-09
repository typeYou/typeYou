from django.db import models


class VerificationCode(models.Model):

    hash_id = models.CharField(
            max_length=8,
    )

    phonenumber = models.CharField(
            max_length=16,
    )

    def __str__(self):
        return self.hash_id
