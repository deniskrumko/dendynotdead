from django.conf.urls import url

from .views import AboutView

urlpatterns = [
    url('^$', AboutView.as_view(), name='index'),
]
