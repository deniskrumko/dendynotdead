from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from .models import News
from django.http import Http404


class NewsView(TemplateView):
    template_name = 'news/list.html'
    news_per_page = 12
    pagination_window = 5

    def _get_paginated_news(self, context, page_id):
        """Method to add pages info to context."""
        all_news = News.objects.order_by('-created')
        if not all_news:
            return context
        p = Paginator(all_news, self.news_per_page)
        cur_page = p.page(page_id)

        center_index = self.pagination_window // 2

        if p.num_pages < self.pagination_window:
            context['pages'] = range(1, p.num_pages+1)
        elif cur_page.number <= center_index + 1:
            context['pages'] = range(1, self.pagination_window + 1)
        elif cur_page.number >= p.num_pages - center_index:
            context['pages'] = range(
                p.num_pages - self.pagination_window + 1, p.num_pages + 1
            )
        else:
            start = cur_page.number - center_index
            context['pages'] = range(start, self.pagination_window + start)

        context['news'] = cur_page.object_list
        context['cur_page'] = cur_page.number

        if cur_page.has_next():
            context['next_page'] = cur_page.next_page_number()
        if cur_page.has_previous():
            context['prev_page'] = cur_page.previous_page_number()

        return context

    def get(self, request, *args, **kwargs):
        """Display ``News`` items with pagination."""
        get_request = super().get(request, args, kwargs)
        context = get_request.context_data
        page_id = request.GET.get('page', 1)
        context = self._get_paginated_news(context, page_id)
        context['active_menu'] = 'Новости'
        context['title'] = 'Dendy Not Dead - Новости'
        return get_request


class SingleNewsView(TemplateView):
    template_name = 'news/single.html'

    def get(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        page_slug = kwargs.get('page_slug')

        news = News.objects.filter(slug=page_slug).first()

        if not news:
            raise Http404("News does not exist")

        context['news'] = news
        context['active_menu'] = 'Новости'
        context['title'] = f'DND - {news.title}'

        news.increment_view()

        return self.render_to_response(context)
