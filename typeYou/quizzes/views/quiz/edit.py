from django.views.generic.detail import DetailView

from quizzes.models import Quiz


class QuizEditView(DetailView):
    model = Quiz
    slug_field = "hash_id"
    template_name = "quiz/edit.html"
    context_object_name = "quiz"

    def get_context_data(self, **kwargs):
        context = super(QuizEditView, self).get_context_data(**kwargs)
        context['site_name'] = "typeYou"

        return context
