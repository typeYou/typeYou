from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import View

from quizzes.models import Quiz


class AnswerSolveView(View):

    def get(self, request, *args, **kwargs):

        hash_id = self.kwargs.get('slug')
        quiz = Quiz.objects.get(hash_id=hash_id)

        if request.user == quiz.user:
            return redirect(reverse("home"))

        return render(
            request,
            "answer/solve.html",
            context={
                "site_name": "typeYou",
                "quiz": quiz,
            })
