from django.conf.urls import url

from .views import NewsView, SingleNewsView

urlpatterns = [
    url('^$', NewsView.as_view(), name='news'),
    url('^(?P<page_slug>[\w-]+)$', SingleNewsView.as_view(), name='single-news'),
]
