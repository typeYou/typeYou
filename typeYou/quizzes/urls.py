from django.conf.urls import url

from quizzes.views import *


urlpatterns = [
    url(r'^$', CreateQuiz.as_view(), name="create"),

    url(r'^(?P<slug>\w+)/$', QuizView.as_view(), name="quiz_detail"),
    url(r'^(?P<slug>\w+)/edit/$', QuizEditView.as_view(), name="quiz_edit"),
    url(r'^(?P<slug>\w+)/publish/$', QuizPublishView.as_view(), name="publish"),

    url(r'^(?P<slug>\w+)/question/create/$', QuizQuestionCreateView.as_view(), name="question_create"),
    url(r'^(?P<slug1>\w+)/question/(?P<slug2>\w+)/edit/$', QuizQuestionEditView.as_view(), name="question_edit"),
    url(r'^(?P<slug1>\w+)/question/(?P<slug2>\w+)/update/$', QuizQuestionUpdateView.as_view(), name="question_update"),
]
