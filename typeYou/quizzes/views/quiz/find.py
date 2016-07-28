from django.contrib import messages
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.shortcuts import render, redirect

from quizzes.models import Quiz


class QuizFindView(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "quiz/find.html",
            context={
                "site_name": "typeYou",
                'quizzes': Quiz.objects.public().filter(is_published=True),
            })

    def post(self, request, *args, **kwargs):

        hash_id = request.POST.get('input_quiz_id')

        try:
            quiz = Quiz.objects.public().get(hash_id=hash_id)
        except ObjectDoesNotExist:
            quiz = None

        if quiz and quiz.is_published:
            return redirect(reverse("quizzes:quiz_detail", kwargs={
                'slug': hash_id
                }))
        else:
            messages.add_message(
                request,
                messages.ERROR,
                settings.ANSWER_FINDING_IS_FAILED_ERROR_MESSAGE,
            )
            return redirect(reverse("quizzes:quiz_find"))
