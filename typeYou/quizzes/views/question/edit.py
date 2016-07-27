from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import View

from quizzes.models import Question, Quiz


class QuizQuestionEditView(View):

    def get(self, request, *args, **kwargs):

        hash_id = self.kwargs.get('slug1')
        quiz = Quiz.objects.public().get(hash_id=hash_id)

        if request.user != quiz.user:
            return redirect(reverse("home"))

        question_id = self.kwargs.get('slug2')
        question = quiz.question_set.public().get(id=question_id)

        return render(
            request,
            "question/edit.html",
            context={
                "site_name": "typeYou",
                "quiz": quiz,
                "question": question,
            })
