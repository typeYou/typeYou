from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http.response import HttpResponse
from django.views.generic import View

from django.contrib.auth.mixins import PermissionRequiredMixin


class CreateQuizView(PermissionRequiredMixin, View):

    permission_required = "users.is_teacher"

    def get(self, request, *args, **kwargs):
        return redirect(reverse("home"))

    def post(self, request, *args, **kwargs):
        new_quiz = request.user.quiz_set.create()

        return redirect(new_quiz)
