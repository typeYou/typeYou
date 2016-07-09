from django.views.generic import View
from django.shortcuts import render, redirect

from users.models import VerificationCode


class TeacherVerification(View):

    def get(self, request, *args, **kwargs):
        return redirect('home')

    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phonenumber = request.POST.get('phonenumber')
        username = request.POST.get('username')
        password = request.POST.get('password')

        code = VerificationCode.objects.create(
                phonenumber=phonenumber,
        )

        return render(
                request,
                'teachers/verification.html',
                {
                    'site_name': 'Verification Code',
                    'first_name': first_name,
                    'last_name': last_name,
                    'phonenumber': phonenumber,
                    'username': username,
                    'password': password,
                    'code': code,
                }
        )
