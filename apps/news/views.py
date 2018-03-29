from django.core.paginator import EmptyPage, Paginator
from django.http.response import Http404
from django.shortcuts import get_object_or_404

from apps.core.views import BaseView

from .models import News


class NewsView(BaseView):
    active_menu = 'Новости'
    news_per_page = 12
    pagination_window = 5
    template_name = 'news/list.html'
    title = 'Dendy Not Dead - Новости'

    def get(self, request, *args, **kwargs):
        """Display ``News`` items with pagination."""
        page = self.get_query_param(request, 'page', default=1)
        context_data = self.get_context_data(page=page)
        return self.render_to_response(context_data)

    def get_context_data(self, page):
        """Method to add pages info to context."""
        context_data = super().get_context_data(page=page)

        if not News.objects.exists():
            return context_data

        p = Paginator(News.objects.all(), self.news_per_page)
        try:
            current_page = p.page(page)
        except EmptyPage:
            raise Http404('Page not found')

        center_index = self.pagination_window // 2

        if p.num_pages < self.pagination_window:
            context_data['pages'] = range(1, p.num_pages+1)
        elif current_page.number <= center_index + 1:
            context_data['pages'] = range(1, self.pagination_window + 1)
        elif current_page.number >= p.num_pages - center_index:
            context_data['pages'] = range(
                p.num_pages - self.pagination_window + 1, p.num_pages + 1
            )
        else:
            start = current_page.number - center_index
            context_data['pages'] = range(
                start, self.pagination_window + start
            )

        context_data['news'] = current_page.object_list
        context_data['cur_page'] = current_page.number

        if current_page.has_next():
            context_data['next_page'] = current_page.next_page_number()

        if current_page.has_previous():
            context_data['prev_page'] = current_page.previous_page_number()

        return context_data


class SingleNewsView(BaseView):
    active_menu = 'Новости'
    template_name = 'news/single.html'

    def get(self, request, **kwargs):
        page_slug = kwargs.get('page_slug')

        news = get_object_or_404(News, slug=page_slug)
        news.increment_view()

        context_data = self.get_context_data(news=news)
        return self.render_to_response(context_data)

    def get_context_data(self, news):
        context_data = super().get_context_data(news=news)
        context_data['news'] = news
        return context_data

    def get_title(self, **kwargs):
        return f'DND - {kwargs["news"].title}'
