from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from users.models import BaseUser, Student


class StudentSignupView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                'students/signup.html',
                {
                    'site_name': 'Student Signup',
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
                        settings.STUDENT_SIGNUP_DUPLICATE_USERNAME_ERROR_MESSAGE,
                )
                return redirect('users:studentsignup')

        student = Student.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                phonenumber=phonenumber,
                username=username,
                password=password,
        )
        messages.add_message(
                request,
                messages.SUCCESS,
                settings.STUDENT_SIGNUP_SUCCESS_MESSAGE,
        )
        return redirect('users:login')
