from django.views.generic import View
from django.shortcuts import render

from quizzes.models import Quiz


class HomeView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                'home.html',
                {
                    'site_name': 'typeYou',
                }
        )
