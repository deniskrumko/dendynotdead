from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView

from apps.music.models import Track
from apps.news.models import News


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'active_menu': 'Главная',
            'tracks': Track.objects.filter(is_active=True)[0:5],
            'news': News.objects.order_by('-created')[0:3],
        }


def handler404(request):
    response = render_to_response('errors/404.html')
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('errors/500.html')
    response.status_code = 500
    return response
