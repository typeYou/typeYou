from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import View

from quizzes.models import Question, Quiz, Solve


class AnswerCreateView(View):

    def get(self, request, *args, **kwargs):
        return redirect(reverse("home"))

    def post(self, request, *args, **kwargs):

        hash_id = self.kwargs.get('slug')
        quiz = Quiz.objects.public().get(hash_id=hash_id)

        if request.user == quiz.user:
            return redirect(reverse("home"))

        if quiz in request.user.solve_quiz_set.public():  # if answer is already submitted
            messages.add_message(
                    request,
                    messages.ERROR,
                    settings.ANSWER_ALREADY_EXIST_ERROR_MESSAGE,
            )
            return redirect(reverse("quizzes:answer_result", kwargs={
                'slug': hash_id,
                })
            )

        for index, question in enumerate(quiz.question_set.public()):
            answer = request.POST.get('answer-{index}'.format(index=index+1))
            q = request.user.answer_set.create(ans=answer, quiz=question.quiz, question=question)

        Solve.objects.create(user=request.user, quiz=quiz)

        messages.add_message(
            request,
            messages.SUCCESS,
            settings.ANSWER_CREATE_SUCCESS_MESSAGE,
        )
        return redirect(reverse("quizzes:answer_result", kwargs={
            'slug': hash_id,
            })
        )
