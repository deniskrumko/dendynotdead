from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView, TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='news/'), name='index'),
    url(r'^news/', include('apps.news.urls')),
    url(r'^music/', include('apps.music.urls')),
    url(r'^about/', include('apps.about.urls')),
    url(r'^search/', include('apps.search.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^test/404/', TemplateView.as_view(template_name='errors/404.html')),
    url(r'^test/500/', TemplateView.as_view(template_name='errors/500.html'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'apps.dendynotdead.views.handler404'
handler500 = 'apps.dendynotdead.views.handler500'
