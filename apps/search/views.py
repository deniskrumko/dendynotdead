from apps.core.views import BaseView


class SearchView(BaseView):
    template_name = 'search/main.html'
    active_menu = 'Поиск'
