from django.views.generic import View
from django.shortcuts import redirect

from quizzes.models import Quiz, Question


class QuizQuestionAnswerUpdateView(View):

    def get(self, request, *args, **kwargs):
        return redirect('home')

    def post(self, request, *args, **kwargs):
        quiz = Quiz.objects.public().get(hash_id=self.kwargs.get('slug1'))

        if request.user != quiz.user:
            return redirect('home')

        question = quiz.question_set.public().get(id=kwargs.get('slug2'))
        answer = request.POST.get('answer')

        question.correct_ans = answer
        question.save()

        return redirect(question)
