from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        from users.signals.post_save import post_save_teacher, post_save_student, post_save_verification
