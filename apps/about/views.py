from django.views.generic.base import TemplateView


class AboutView(TemplateView):
    template_name = 'about/main.html'

    def get_context_data(self, **kwargs):
        return {
            'active_menu': 'О проекте',
        }
