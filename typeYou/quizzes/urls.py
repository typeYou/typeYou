from django.conf.urls import url

from quizzes.views import *


urlpatterns = [
    url(r'^$', CreateQuiz.as_view(), name="create"),
]
