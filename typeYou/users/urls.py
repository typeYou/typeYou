from django.conf.urls import url

from users.views import *


urlpatterns = [
    url(r'^teachers/signup/$', TeacherSignupView.as_view(), name='teachersignup'),

]
