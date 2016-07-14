from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import View

from quizzes.models import Question, Quiz


class QuizQuestionDeleteView(View):

    def get(self, request, *args, **kwargs):

        hash_id = self.kwargs.get('slug1')
        quiz = Quiz.objects.get(hash_id=hash_id)

        if request.user != quiz.user:
            return redirect(reverse("home"))

        question_id = self.kwargs.get('slug2')
        question = quiz.question_set.get(id=question_id)

        question.delete()

        return redirect(reverse("quizzes:quiz_edit", kwargs={
            "slug": quiz.hash_id,
        }))
