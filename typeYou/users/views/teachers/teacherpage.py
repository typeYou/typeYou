from django.views.generic import View
from django.shortcuts import render, redirect

from users.models import BaseUser


class TeacherPageView(View):
    slug_field = 'username'

    def get(self, request, *args, **kwargs):
        username = self.kwargs.get('slug')

        if request.user.username == username:
            if request.user.has_perm('users.is_teacher'):
                return redirect('users:teachermypage')
            elif request.user.has_perm('users.is_student'):
                return redirect('users:studentmypage')
        return render(
                request,
                'teachers/teacherpage.html',
                {
                    'site_name': '{username}'.format(username=username),
                    'user': BaseUser.objects.get(username=username),
                }
        )
