from django.db import models
from django.core.urlresolvers import reverse


class Follow(models.Model):

    follower = models.ForeignKey(
            'BaseUser',
            related_name='+',
    )

    following = models.ForeignKey(
            'BaseUser',
            related_name='+',
    )

    def get_absolute_url(self):
        return reverse(
                'users:teacherpage',
                kwargs={
                    'slug': self.following,
                }
        )
