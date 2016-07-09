from django.views.generic import View
from django.contrib.auth import logout
from django.shortcuts import redirect


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('users:login')
