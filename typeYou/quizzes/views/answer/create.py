from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import View

from quizzes.models import Question, Quiz, Solve


class AnswerCreateView(View):

    def get(self, request, *args, **kwargs):
        return redirect(reverse("home"))

    def post(self, request, *args, **kwargs):

        hash_id = self.kwargs.get('slug')
        quiz = Quiz.objects.get(hash_id=hash_id)

        if request.user == quiz.user:
            return redirect(reverse("home"))

        # TODO: prevent Answer submit if it exist already
        if quiz in request.user.solve_quiz_set.all():  # if answer is already submitted
            pass

        for index, question in enumerate(quiz.question_set.public()):
            answer = request.POST.get('answer-{index}'.format(index=index+1))
            q = request.user.answer_set.create(ans=answer, quiz=question.quiz, question=question)

        Solve.objects.create(user=request.user, quiz=quiz)

        return redirect("/login/")  # TODO: fix to direct correctly
