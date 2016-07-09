from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

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
                return redirect('users:teachermypage')
            elif user.has_perm('users.is_student'):
                login(request, user)
                return redirect('users:studentmypage')
            return redirect('users:login')
        return redirect('users:login')
