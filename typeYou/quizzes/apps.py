from django.apps import AppConfig


class QuizzesConfig(AppConfig):
    name = 'quizzes'

    def ready(self):
        from quizzes.signals.post_save import post_save_quiz
