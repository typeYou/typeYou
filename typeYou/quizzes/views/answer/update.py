from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import View

from quizzes.models import Question, Quiz, Solve


class AnswerUpdateView(View):

    def get(self, request, *args, **kwargs):
        return redirect(reverse("home"))

    def post(self, request, *args, **kwargs):

        hash_id = self.kwargs.get('slug')
        quiz = Quiz.objects.get(hash_id=hash_id)

        if request.user == quiz.user:
            return redirect(reverse("home"))

        if quiz not in request.user.solve_quiz_set.all():  # if submitted answer does not exist
            messages.add_message(
                request,
                messages.ERROR,
                settings.ANSWER_DOES_NOT_EXIST_ERROR_MESSAGE,
            )
            return redirect(reverse("quizzes:quiz_detail", kwargs={
                'slug': hash_id,
                })
            )

        answers = quiz.answer_set.filter(user=request.user)

        for index, answer in enumerate(answers):
            data_from_post_get = request.POST.get('answer-{index}'.format(index=index+1))
            answer.ans = data_from_post_get
            answer.save()

        messages.add_message(
            request,
            messages.SUCCESS,
            settings.ANSWER_UPDATE_SUCCESS_MESSAGE,
        )
        return redirect(reverse("quizzes:answer_result", kwargs={
            'slug': hash_id,
            })
        )
