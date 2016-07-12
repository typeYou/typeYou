from django.conf.urls import url

from users.views import *


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^teachers/signup/$', TeacherSignupView.as_view(), name='teachersignup'),
    url(r'^teachers/mypage/$', TeacherMyPageView.as_view(), name='teachermypage'),
    url(r'^teachers/verification/$', TeacherVerification.as_view(), name='teacherverification'),

    url(r'^students/signup/$', StudentSignupView.as_view(), name='studentsignup'),
    url(r'^students/mypage/$', StudentMyPageView.as_view(), name='studentmypage'),
    url(r'^students/verification/$', StudentVerification.as_view(), name='studentverification'),

]
