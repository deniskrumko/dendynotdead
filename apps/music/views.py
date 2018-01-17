from django.views.generic.base import TemplateView
from django.http import Http404

from .models import Track, File


class TrackListView(TemplateView):
    """View to display list of tracks."""
    template_name = 'music/list.html'
    queryset = Track.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        return {
            'tracks': self.queryset,
            'active_menu': 'Музыка',
        }


class TrackView(TemplateView):
    """View to see a single track."""
    template_name = 'music/single.html'
    queryset = Track.objects.filter(is_active=True)

    def get(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        page_slug = kwargs.get('track_slug')

        track = self.queryset.filter(slug=page_slug).first()

        if not track:
            raise Http404("Track does not exist")

        context['track'] = track
        context['active_menu'] = 'Музыка'

        context['extra_files'] = [
            (name, track.extra_files.filter(file__category=key))
            for key, name in File.CATEGORIES
        ] if track.extra_files.exists() else None

        return self.render_to_response(context)
