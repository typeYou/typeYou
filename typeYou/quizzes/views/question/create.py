from django.views.generic import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from quizzes.models import Question, Quiz


class QuizQuestionCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'users.is_teacher'
    model = Question
    fields = [
        'title',
        'ans1',
        'ans2',
        'ans3',
        'ans4',
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.quiz = Quiz.objects.get(
                hash_id=self.kwargs.get('slug'),
        )
        return super(QuizQuestionCreateView, self).form_valid(form)
