from django.views.generic.base import TemplateView

from .models import AboutInfo


class AboutView(TemplateView):
    template_name = 'about/main.html'

    def get_context_data(self, **kwargs):
        return {
            'active_menu': 'О проекте',
            'title': 'Dendy Not Dead - О проекте',
            'info': AboutInfo.objects.all(),
        }
