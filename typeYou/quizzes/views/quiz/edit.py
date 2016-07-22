from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic.detail import View

from quizzes.models import Quiz


class QuizEditView(View):

    def get(self, request, *args, **kwargs):

        hash_id = self.kwargs.get('slug')
        quiz = Quiz.objects.public().get(hash_id=hash_id)

        if request.user != quiz.user:
            return redirect(reverse("home"))

        return render(
            request,
            "quiz/edit.html",
            context={
                "site_name": "typeYou",
                "quiz": Quiz.objects.public().get(hash_id=self.kwargs.get("slug")),
                "is_quiz_edit_page": True,
            })
