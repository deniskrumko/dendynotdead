from django.shortcuts import redirect
from django.views.generic.base import TemplateView

from libs.views import BaseViewMixin

from .models import WallMessage

base_css = ['fonts.css', 'shortcuts.css', 'logo.css', 'cd-top.css']


class WallView(BaseViewMixin, TemplateView):
    """View class for ``The Wall`` page."""
    menu_section = 'wall'
    template_name = 'wall.html'
    title = 'DND — The Wall'
    import_js = ['base.js', 'cd-top.js']
    import_css = base_css + ['body.css', 'menu.css', 'wall.css']

    def get(self, request, *args, **kwargs):
        """Display all ``WallMessage`` objects."""
        get_request = super().get(request, args, kwargs)
        context = get_request.context_data
        context['messages'] = WallMessage.objects.order_by('id').reverse()
        context['session_id'] = request.session.session_key
        return get_request

    def post(self, request, *args, **kwargs):
        """Add new ``WallMessage`` object."""

        delete_msg = request.POST.get('delete_msg')
        msg = request.POST.get('message')

        if delete_msg:
            qs = WallMessage.objects.filter(id=int(delete_msg))
            if qs.exists():
                qs.delete()

        elif msg and len(msg) > 0:
            if not request.session.session_key:
                request.session.cycle_key()
            session_id = request.session.session_key
            WallMessage.objects.create(message=msg, session_id=session_id)

        return super().post(request, args, kwargs)
