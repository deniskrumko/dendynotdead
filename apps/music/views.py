from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from .models import File, Track
from apps.core.views import BaseView


class TrackListView(TemplateView):
    """View to display list of tracks."""
    template_name = 'music/list.html'
    active_menu = 'Музыка'
    title = 'Dendy Not Dead - Музыка'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['tracks'] = Track.objects.filter(is_active=True)
        return context_data


class TrackView(BaseView):
    """View to see a single track."""
    template_name = 'music/single.html'
    active_menu = 'Музыка'

    def get_title(self, **kwargs):
        return f'DND - {kwargs["track"].name}'

    def get_context_data(self, track):
        context_data = super().get_context_data(track=track)
        context_data['track'] = track
        context_data['next_track'] = track.get_previous()
        context_data['prev_track'] = track.get_next()
        context_data['extra_files'] = [
            (name, track.extra_files.filter(file__category=key))
            for key, name in File.CATEGORIES
        ] if track.extra_files.exists() else None
        return context_data

    def get(self, request, **kwargs):
        page_slug = kwargs.get('track_slug')
        track = get_object_or_404(Track, is_active=True, slug=page_slug)
        context = self.get_context_data(track=track)
        return self.render_to_response(context)
