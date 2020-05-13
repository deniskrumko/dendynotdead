from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.core.paginator import Paginator
from libs.views import BaseViewMixin

from .models import AudioTrack
from . import DND, DK

base_css = ['fonts.css', 'shortcuts.css', 'logo.css', 'cd-top.css']


class ExploreView(BaseViewMixin, TemplateView):
    template_name = 'explore.html'
    title = 'DND — Explore'
    menu_section = 'explore'
    import_js = ['explore.js', 'base.js', 'cd-top.js']
    import_css = base_css + ['body.css', 'explore.css', 'rail.css', 'menu.css']

    def get(self, request, *args, **kwargs):
        get_request = super().get(request, args, kwargs)
        context = get_request.context_data

        context['dnd_tracks'] = AudioTrack.objects.filter(artist=DND)
        context['dk_tracks'] = AudioTrack.objects.filter(artist=DK)

        return get_request

    def post(self, request, *args, **kwargs):
        like = request.POST.get('like')
        if like:
            track_id = int(like)
            audio_track = AudioTrack.objects.get(id=track_id)
            audio_track.inc_like()
            audio_track.save()
            return HttpResponse('')

        return super().post(request, args, kwargs)


class SingleView(BaseViewMixin, TemplateView):
    template_name = 'single.html'
    menu_section = 'explore'
    title = 'DND — Explore'  # TODO: different track names
    import_js = ['base.js']
    import_css = base_css + ['body.css', 'menu.css', 'single.css']

    def get(self, request, *args, **kwargs):
        get_request = super().get(request, args, kwargs)
        context = get_request.context_data

        track_id = kwargs.get('track_id')
        context['track'] = AudioTrack.objects.get(id=track_id)

        all_news = AudioTrack.objects.all().order_by('id')
        p = Paginator(all_news, 1)
        cur_page = p.page(track_id)

        if cur_page.has_next():
            next_song = p.page(cur_page.next_page_number())
            context['next_song'] = next_song.object_list[0].track_name
            context['next_song_id'] = cur_page.next_page_number()

        if cur_page.has_previous():
            prev_song = p.page(cur_page.previous_page_number())
            context['prev_song'] = prev_song.object_list[0].track_name
            context['prev_song_id'] = cur_page.previous_page_number()

        return get_request
