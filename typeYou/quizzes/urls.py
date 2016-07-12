from django.conf.urls import url

from quizzes.views import *


urlpatterns = [
    url(r'^$', CreateQuiz.as_view(), name="create"),

    url(r'^(?P<slug>\w+)/$', QuizDetailView.as_view(), name="quiz_detail"),
]
