from django.views.generic.base import TemplateView


class SearchView(TemplateView):
    template_name = 'search/main.html'

    def get_context_data(self, **kwargs):
        return {
            'active_menu': 'Поиск',
        }
