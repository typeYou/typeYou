from django.conf.urls import url, include
from django.contrib import admin

from typeYou.views import home


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # typeYou Urls
    url(r'^$', home, name='home'),

    # Included Apps Urls
    url(r'^', include('users.urls', namespace='users')),
    url(r'^quizzes/', include('quizzes.urls', namespace='quizzes')),
]
