from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='news/'), name='index'),
    url(r'^news/', include('apps.news.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
