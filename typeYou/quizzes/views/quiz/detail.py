from django.views.generic.detail import DetailView

from quizzes.models import Quiz


class QuizDetailView(DetailView):
    model = Quiz
    slug_field = "hash_id"
    template_name = "quiz/detail.html"
    context_object_name = "quiz"

    def get_context_data(self, **kwargs):
        context = super(QuizDetailView, self).get_context_data(**kwargs)
        context['site_name'] = "typeYou"

        return context
