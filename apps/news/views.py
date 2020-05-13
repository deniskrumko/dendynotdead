from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from libs.views import BaseViewMixin
from django.http import HttpResponse
from django.conf import settings

from .models import News

base_css = ['fonts.css', 'shortcuts.css', 'logo.css', 'cd-top.css']


class NewsView(BaseViewMixin, TemplateView):
    """View for ``News`` page."""
    menu_section = 'news'
    template_name = 'news.html'
    title = 'DND — News'
    import_js = ['base.js', 'news.js']
    import_css = base_css + ['body.css', 'menu.css', 'news.css']

    def _get_paginated_news(self, context, page_id):
        """Method to add pages info to context."""
        all_news = News.objects.all().order_by('id').reverse()
        p = Paginator(all_news, settings.NEWS_PER_PAGE)
        cur_page = p.page(page_id)
        if cur_page.has_next():
            context['next_page'] = cur_page.next_page_number()
        if cur_page.has_previous():
            context['prev_page'] = cur_page.previous_page_number()
        context['news'] = cur_page.object_list
        context['cur_page'] = str(cur_page)[1:-1]
        return context

    def get(self, request, *args, **kwargs):
        """Display ``News`` items with pagination."""
        get_request = super().get(request, args, kwargs)
        context = get_request.context_data

        page_id = kwargs.get('page_id')
        context = self._get_paginated_news(context, page_id)
        return get_request

    def post(self, request, *args, **kwargs):
        """Increase amount of likes for specific news."""
        like = request.POST.get('like')
        if like:
            news_item = News.objects.get(id=int(like))
            news_item.inc_like()
            news_item.save()
            return HttpResponse('')

        return super().post(request, args, kwargs)
