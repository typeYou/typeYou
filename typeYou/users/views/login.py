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
            login(request, user)
            return redirect('home')
        return redirect('users:login')
