from django.conf.urls import url

from quizzes.views import *


urlpatterns = [
    url(r'^create/$', CreateQuizView.as_view(), name="create"),
    url(r'^(?P<slug>\w+)/$', QuizView.as_view(), name="quiz_detail"),
    url(r'^(?P<slug>\w+)/edit/$', QuizEditView.as_view(), name="quiz_edit"),
    url(r'^(?P<slug>\w+)/publish/$', QuizPublishView.as_view(), name="publish"),
    url(r'^(?P<slug>\w+)/marking/$', QuizMarkingView.as_view(), name="quiz_marking"),

    url(r'^(?P<slug>\w+)/question/create/$', QuizQuestionCreateView.as_view(), name="question_create"),
    url(r'^(?P<slug1>\w+)/question/(?P<slug2>\w+)/edit/$', QuizQuestionEditView.as_view(), name="question_edit"),
    url(r'^(?P<slug1>\w+)/question/(?P<slug2>\w+)/update/$', QuizQuestionUpdateView.as_view(), name="question_update"),
    url(r'^(?P<slug1>\w+)/question/(?P<slug2>\w+)/delete/$', QuizQuestionDeleteView.as_view(), name="question_delete"),
    url(r'^(?P<slug1>\w+)/question/(?P<slug2>\w+)/correct_ans_update/$', QuizQuestionAnswerUpdateView.as_view(), name="question_answer_update"),

    url(r'^(?P<slug>\w+)/answer/solve/$', AnswerSolveView.as_view(), name="answer_solve"),
    url(r'^(?P<slug>\w+)/answer/create/$', AnswerCreateView.as_view(), name="answer_create"),
    url(r'^(?P<slug>\w+)/answer/result/$', AnswerResultView.as_view(), name="answer_result"),
    url(r'^(?P<slug>\w+)/answer/result/before_marking/$', AnswerResultBeforeMarkingView.as_view(), name="result_before_marking"),
    url(r'^(?P<slug>\w+)/answer/edit/$', AnswerEditView.as_view(), name="answer_edit"),
    url(r'^(?P<slug>\w+)/answer/update/$', AnswerUpdateView.as_view(), name="answer_update"),
    url(r'^(?P<slug>\w+)/answer/delete/$', AnswerDeleteView.as_view(), name="answer_delete"),
]
