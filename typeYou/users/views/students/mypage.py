from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class StudentMyPageView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'students/mypage.html'
    permission_required = 'users.is_student'

    def get_context_data(self, **kwargs):
        context = super(StudentMyPageView, self).get_context_data(**kwargs)
        context['site_name'] = 'Student MyPage'
        return context
