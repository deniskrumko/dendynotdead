from apps.core.views import BaseView

from .models import AboutInfo


class AboutView(BaseView):
    template_name = 'about/main.html'
    active_menu = 'О проекте'
    title = 'Dendy Not Dead - О проекте'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['info'] = AboutInfo.objects.all()
        return context_data
