from django.views.generic import View
from django.shortcuts import render, redirect

from users.models import Teacher


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

        teacher = Teacher.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                phonenumber=phonenumber,
                username=username,
                password=password,
        )

        return redirect('home')
