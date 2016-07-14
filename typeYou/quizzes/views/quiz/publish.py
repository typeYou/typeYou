from django.views.generic.edit import UpdateView

from quizzes.models import Quiz


class QuizPublishView(UpdateView):
    model = Quiz
    slug_field = 'hash_id'
    template_name = 'quiz/edit.html'
    fields = [
    ]

    def form_valid(self, form):
        form.instance.is_published = True
        return super(QuizPublishView, self).form_valid(form)
