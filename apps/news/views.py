from django.views.generic.base import TemplateView

from .models import News


class NewsView(TemplateView):
    template_name = 'news.html'

    def get_context_data(self, *args, **kwargs):
        return {
            'news': News.objects.all()
        }


class SingleNewsView(TemplateView):
    template_name = 'single_news.html'

    def get(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        page_slug = kwargs.get('page_slug')

        news = News.objects.filter(slug=page_slug).first()

        if news:
            context['news'] = news
            return self.render_to_response(context)
