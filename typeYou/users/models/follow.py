from django.db import models


class Follow(models.Model):

    follower = models.ForeignKey(
            'BaseUser',
            related_name='+',
    )

    following = models.ForeignKey(
            'BaseUser',
            related_name='+',
    )
