from django.contrib import admin

from .models import Track, File, TrackFile


class TrackFileInline(admin.TabularInline):
    """Inline class for ``TrackFile`` model."""
    model = TrackFile
    extra = 0


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )
    inlines = (TrackFileInline,)


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
