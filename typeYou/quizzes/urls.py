from django.conf.urls import url

from quizzes.views import *


urlpatterns = [
    url(r'^$', CreateQuiz.as_view(), name="create"),

    url(r'^(?P<slug>\w+)/$', QuizView.as_view(), name="quiz_detail"),
    url(r'^(?P<slug>\w+)/edit/$', QuizEditView.as_view(), name="quiz_edit"),

    url(r'^(?P<slug>\w+)/create/$', QuizQuestionCreateView.as_view(), name="question_create"),
]
