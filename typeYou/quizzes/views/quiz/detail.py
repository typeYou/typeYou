from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic.detail import View

from quizzes.models import Quiz


class QuizView(View):

    def get(self, request, *args, **kwargs):

        hash_id = self.kwargs.get('slug')
        quiz = Quiz.objects.public().get(hash_id=hash_id)

        if request.user == quiz.user:
            if not quiz.is_published:
                return redirect(reverse("quizzes:quiz_edit", kwargs={
                    'slug': hash_id,
                }))

        return render(
            request,
            "quiz/detail.html",
            context={
                "site_name": "typeYou",
                "quiz": Quiz.objects.public().get(hash_id=self.kwargs.get("slug")),
                "quiz_detail_page": True,
            })
