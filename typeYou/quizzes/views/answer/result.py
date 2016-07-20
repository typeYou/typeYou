from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import View


class AnswerResultView(View):

    def get(self, request, *args, **kwargs):

        hash_id = self.kwargs.get('slug')

        # Exception for a possibility of which user hasn't solved this quiz but access this page.
        try:
            quiz = request.user.solve_quiz_set.get(hash_id=hash_id)
        except ObjectDoesNotExist:
            quiz = None

        if quiz:
            answers = quiz.answer_set.filter(user=request.user)
            # if there is not a been making question, redirect user to before_marking page
            for answer in answers:
                if answer.correct is None:
                    return redirect(reverse(
                        "quizzes:result_before_marking",
                        kwargs={
                            "slug": hash_id,
                        })
                    )

            # TODO: if making by quiz's owner has done, show some statistic information

        else:
            # TODO: There is no solved quiz by request.user. redirect anywhere.
            pass
