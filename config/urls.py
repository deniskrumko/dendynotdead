from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView

from apps.dendynotdead.views import IndexView, AboutView
from apps.audiofiles.views import ExploreView, SingleView
from apps.news.views import NewsView
from apps.wall.views import WallView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^explore/$', ExploreView.as_view(), name='explore'),
    url(r'^explore/(?P<track_id>\d+)/$', SingleView.as_view(), name='single'),
    url(r'^news/$', RedirectView.as_view(url='/news/1/')),
    url(r'^news/(?P<page_id>\d+)/$', NewsView.as_view(), name='news'),
    url(r'^wall/$', WallView.as_view(), name='wall'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
