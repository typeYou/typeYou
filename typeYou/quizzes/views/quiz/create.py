from django.http.response import HttpResponse
from django.views.generic import View


class CreateQuiz(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("CreateQuiz")
