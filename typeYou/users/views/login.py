from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.conf import settings

from users.models import BaseUser


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                'login.html',
                {
                    'site_name': 'typeYou Login',
                }
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_page = request.POST.get('next_page')

        user = authenticate(
                username=username,
                password=password,
        )

        if user:
            if user.has_perm('users.is_teacher'):
                login(request, user)
                messages.add_message(
                        request,
                        messages.SUCCESS,
                        settings.TEACHER_LOGIN_SUCCESS_MESSAGE,
                )
                return redirect('users:teachermypage')
            elif user.has_perm('users.is_student'):
                login(request, user)
                messages.add_message(
                        request,
                        messages.SUCCESS,
                        settings.STUDENT_LOGIN_SUCCESS_MESSAGE,
                )
                return redirect('users:studentmypage')
        messages.add_message(
                request,
                messages.ERROR,
                settings.LOGIN_ERROR_MESSAGE,
        )
        return redirect('users:login')
