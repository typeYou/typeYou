from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class TeacherMyPageView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'teachers/mypage.html'
    permission_required = 'users.is_teacher'

    def get_context_data(self, **kwargs):
        context = super(TeacherMyPageView, self).get_context_data(**kwargs)
        context['site_name'] = 'Teacher MyPage'
        return context
