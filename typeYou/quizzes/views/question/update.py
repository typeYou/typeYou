from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import View

from quizzes.models import Question, Quiz


class QuizQuestionUpdateView(View):

    def get(self, request, *args, **kwargs):
        return redirect(reverse("home"))

    def post(self, request, *args, **kwargs):

        hash_id = self.kwargs.get('slug1')
        quiz = Quiz.objects.public().get(hash_id=hash_id)

        if request.user != quiz.user:
            return redirect(reverse("home"))

        question_id = self.kwargs.get('slug2')
        question = quiz.question_set.public().get(id=question_id)

        title = request.POST.get("title")
        ans1 = request.POST.get("ans1")
        ans2 = request.POST.get("ans2")
        ans3 = request.POST.get("ans3")
        ans4 = request.POST.get("ans4")

        question.title = title
        question.ans1 = ans1
        question.ans2 = ans2
        question.ans3 = ans3
        question.ans4 = ans4

        question.save()

        return redirect(question)
