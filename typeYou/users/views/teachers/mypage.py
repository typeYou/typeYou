from django.views.generic import TemplateView


class TeacherMyPageView(TemplateView):
    template_name = 'teachers/mypage.html'

    def get_context_data(self, **kwargs):
        context = super(TeacherMyPage, self).get_context_data(**kwargs)
        context['site_name'] = 'Teacher MyPage'
        return context
