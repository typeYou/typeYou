from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.views.generic import View


class AnswerEditView(View):

    def get(self, request, *args, **kwargs):

        hash_id = self.kwargs.get('slug')

        # Exception for a possibility of which user hasn't solved this quiz but access this page.
        try:
            quiz = request.user.solve_quiz_set.public().get(hash_id=hash_id)
        except ObjectDoesNotExist:
            quiz = None

        if not quiz:
            messages.add_message(
                request,
                messages.ERROR,
                settings.ANSWER_DOES_NOT_EXIST_ERROR_MESSAGE
            )

            return redirect(reverse("quizzes:quiz_detail", kwargs={
                "slug": hash_id,
                })
            )

        answers = quiz.answer_set.public().filter(user=request.user)

        return render(
            request,
            "answer/edit.html",
            context={
                "site_name": "typeYou",
                "quiz": quiz,
                "answers": answers,
            }
        )
