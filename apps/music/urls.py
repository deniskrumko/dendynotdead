from django.conf.urls import url

from .views import TrackListView, TrackView

urlpatterns = [
    url('^$', TrackListView.as_view(), name='track-list'),
    url('^(?P<track_slug>[\w-]+)/$', TrackView.as_view(), name='track'),
]
