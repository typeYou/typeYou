from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.conf import settings

from users.models import BaseUser, Follow


class FollowCreateView(LoginRequiredMixin, CreateView):
    model = Follow
    fields = [
    ]

    def form_valid(self, form):
        follower = self.request.user
        following = BaseUser.objects.get(
                username=self.request.POST.get('username')
        )
        # TODO: ensure that FollowCreateView object can only be created once

        form.instance.follower = follower
        form.instance.following = following

        messages.add_message(
                self.request,
                messages.SUCCESS,
                settings.FOLLOW_SUCCESS_MESSAGE,
        )
        return super(FollowCreateView, self).form_valid(form)
