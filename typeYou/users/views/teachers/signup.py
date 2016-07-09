from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from users.models import BaseUser, Teacher


class TeacherSignupView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                'teachers/signup.html',
                {
                    'site_name': 'Teacher Signup',
                }
        )

    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phonenumber = request.POST.get('phonenumber')
        username = request.POST.get('username')
        password = request.POST.get('password')

        for user in BaseUser.objects.all():
            if user.username == username:
                messages.add_message(
                        request,
                        messages.ERROR,
                        settings.TEACHER_SIGNUP_DUPLICATE_USERNAME_ERROR_MESSAGE,
                )
                return redirect('users:teachersignup')

        teacher = Teacher.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                phonenumber=phonenumber,
                username=username,
                password=password,
        )
        messages.add_message(
                request,
                messages.SUCCESS,
                settings.TEACHER_SIGNUP_SUCCESS_MESSAGE,
        )
        return redirect('users:login')
