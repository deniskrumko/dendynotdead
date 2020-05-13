from django.contrib import admin

from .models import AudioTrack, AudioFile


class AudioFileInline(admin.StackedInline):
    model = AudioFile
    extra = 0
    fields = (
        'file_mp3', 'file_ogg', 'file_wav', 'version', 'main_priority'
    )


class AudioFileAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'parent_track', 'version', 'main_priority'
    )
    fieldsets = (
        (None, {
            'fields': (
                'parent_track',
                'version',
                'main_priority'
            )
        }),
        ('Files', {
            'fields': (
                'file_mp3',
                'file_ogg',
                'file_wav',
            )
        }),
    )


class AudioTrackAdmin(admin.ModelAdmin):
    list_display = ('track_name', 'artist', 'published', 'likes')
    readonly_fields = ('id', 'likes')
    fieldsets = (
        (None, {
            'fields': (
                'track_name',
                'artist'
            )
        }),
        ('INFORMATION', {
            'fields': (
                'description_ru',
                'description_en',
                'lyrics',
                'published',
                'youtube_link',
                'likes',
            )
        }),
        ('GTP FILE', {
            'fields': ('gtp_file',)
        }),
    )
    inlines = [AudioFileInline]


admin.site.register(AudioTrack, AudioTrackAdmin)
admin.site.register(AudioFile, AudioFileAdmin)
