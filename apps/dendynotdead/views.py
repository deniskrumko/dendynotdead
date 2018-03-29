from django.shortcuts import render_to_response

from apps.core.views import BaseView
from apps.music.models import Track
from apps.news.models import News


class IndexView(BaseView):
    template_name = 'index.html'
    active_menu = 'Главная'
    title = 'Dendy Not Dead - Главная'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['tracks'] = Track.objects.filter(is_active=True)[0:5]
        context_data['news'] = News.objects.all()[0:3]
        return context_data


def handler404(request):
    response = render_to_response('errors/404.html')
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('errors/500.html')
    response.status_code = 500
    return response
