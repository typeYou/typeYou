from django.views.generic.detail import View
from django.shortcuts import render

from quizzes.models import Quiz


class QuizView(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "quiz/detail.html",
            context={
                "site_name": "typeYou",
                "quiz": Quiz.objects.get(hash_id=self.kwargs.get("slug")),
            })
