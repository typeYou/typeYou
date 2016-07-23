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
        quiz = Quiz.objects.public().get(hash_id=hash_id)

        if request.user == quiz.user:
            return redirect(reverse("home"))

        if quiz not in request.user.solve_quiz_set.public():  # if submitted answer does not exist
            messages.add_message(
                request,
                messages.ERROR,
                settings.ANSWER_DOES_NOT_EXIST_ERROR_MESSAGE,
            )
            return redirect(reverse("quizzes:quiz_detail", kwargs={
                'slug': hash_id,
                })
            )

        answers = quiz.answer_set.public().filter(user=request.user)

        for index, _ in enumerate(quiz.question_set.public()):
            answer_data = request.POST.get('answer-{index}'.format(index=index+1))
            question_id = request.POST.get('question-{index}'.format(index=index+1))
            question = Question.objects.public().get(id=question_id)
            answer = question.answer_set.public().get(user=request.user)
            answer.ans = answer_data
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
