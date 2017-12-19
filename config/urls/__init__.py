from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='news/'), name='index'),
    path('news/', include('apps.news.urls')),
    path('admin/', admin.site.urls),
]
