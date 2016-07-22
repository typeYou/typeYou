from django.conf import settings
from django.contrib import messages
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

        # if quiz is already submitted, redirect to result page
        if quiz in request.user.solve_quiz_set.filter(hash_id=hash_id):
            messages.add_message(
                    request,
                    messages.ERROR,
                    settings.ANSWER_ALREADY_EXIST_ERROR_MESSAGE,
            )
            return redirect(
                reverse(
                    "quizzes:answer_result",
                    kwargs={
                        'slug': hash_id,
                    }
                )
            )

        return render(
            request,
            "answer/solve.html",
            context={
                "site_name": "typeYou",
                "quiz": quiz,
            })
