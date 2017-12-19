from django.views.generic.base import TemplateView

from .models import News


class NewsView(TemplateView):
    template_name = 'news.html'

    def get_context_data(self, *args, **kwargs):
        return {
            'news': News.objects.all()
        }
