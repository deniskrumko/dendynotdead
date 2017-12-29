from django.views.generic.base import TemplateView
from django.http import Http404

from .models import Track


class TrackListView(TemplateView):
    template_name = 'music/list.html'

    def get_context_data(self, **kwargs):
        return {
            'tracks': Track.objects.all(),
            'active_menu': 'Музыка',
        }


class TrackView(TemplateView):
    template_name = 'music/single.html'

    def get(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        page_slug = kwargs.get('track_slug')

        track = Track.objects.filter(slug=page_slug).first()

        if not track:
            raise Http404("Track does not exist")

        context['track'] = track
        context['active_menu'] = 'Музыка'
        return self.render_to_response(context)
