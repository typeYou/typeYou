from django.views.generic import View
from django.shortcuts import render

from quizzes.models import Quiz
from quizzes.utils.nvd3 import create_chart_data_set


class QuizResultView(View):

    def get(self, request, *args, **kwargs):

        hash_id = self.kwargs.get('slug')
        quiz = Quiz.objects.public().get(hash_id=hash_id)

        questions = quiz.question_set.public()

        chart_data_set = create_chart_data_set(quiz)

        return render(
            request,
            "quiz/result.html",
            context={
                "site_name": "typeYou",
                "quiz": quiz,
                "questions": questions,
                "chart_data_set": chart_data_set,
            },
        )
