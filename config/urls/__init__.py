from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import ugettext_lazy as _

admin.site.site_header = _('Dendy Not Dead')
admin.site.site_title = _('DND')

urlpatterns = [
    # Apps
    url('', include('apps.dendynotdead.urls', namespace='main')),
    url(r'^news/', include('apps.news.urls', namespace='news')),
    url(r'^music/', include('apps.music.urls', namespace='music')),
    url(r'^about/', include('apps.about.urls', namespace='about')),
    url(r'^search/', include('apps.search.urls', namespace='search')),

    # Admin UI
    url(r'^admin/', admin.site.urls),

    # Testing views
    url(r'^test/404/', TemplateView.as_view(template_name='errors/404.html')),
    url(r'^test/500/', TemplateView.as_view(template_name='errors/500.html'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'apps.dendynotdead.views.handler404'
handler500 = 'apps.dendynotdead.views.handler500'
