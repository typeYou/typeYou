from django.contrib import messages
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import View

from quizzes.models import Quiz


class QuizMarkingView(View):

    def get(self, request, *args, **kwargs):

        hash_id = self.kwargs.get('slug')
        quiz = Quiz.objects.public().get(hash_id=hash_id)

        if request.user != quiz.user or not quiz.is_published:
            return redirect(reverse("quizzes:quiz_edit", kwargs={
                'slug': hash_id,
            }))

        from quizzes.tasks import MarkingTask
        marking = MarkingTask()
        marking.run(quiz)
        # we don't use asynchronous function for answers marking feature
        # it is because answers marking should let the quiz owner know if it finished

        if quiz.is_marked is True:
            messages.add_message(
                request,
                messages.SUCCESS,
                settings.ANSWER_MARKING_SUCCESS_MESSAGE,
            )
        # FIXME: This feature works even if it is on exceptional circumstances
        # someday, make this feature work properly

        return redirect(reverse("quizzes:quiz_result", kwargs={
            'slug': hash_id,
            })
        )
