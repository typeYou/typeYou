from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.generic import View


class AnswerResultBeforeMarkingView(View):

    def get(self, request, *args, **kwargs):

        hash_id = self.kwargs.get('slug')
        editable = False

        # Exception for a possibility of which user hasn't solved this quiz but access this page.
        try:
            quiz = request.user.solve_quiz_set.get(hash_id=hash_id)
        except ObjectDoesNotExist:
            quiz = None

        answers = quiz.answer_set.public().filter(user=request.user)

        # if answers are not marked by Quiz owner,
        if quiz.answer_set.filter(correct=None):
            editable = True

        return render(
            request,
            "answer/result_before_marking.html",
            context={
                "site_name": "typeYou",
                "quiz": quiz,
                "answers": answers,
                "editable": editable,
            }
        )
