from django.contrib import admin
from django.http.response import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from adminsortable.admin import SortableAdmin
from django_object_actions import (
    DjangoObjectActions,
    takes_instance_or_queryset,
)

from apps.core.admin import image_preview

from .forms import TrackForm
from .models import File, Track, TrackFile


class TrackFileInline(admin.TabularInline):
    """Inline class for ``TrackFile`` model."""
    model = TrackFile
    extra = 0


@admin.register(Track)
class TrackAdmin(DjangoObjectActions, SortableAdmin):
    """Admin class for ``Track`` model."""
    sortable_change_list_with_sort_link_template = (
        'django_object_actions/change_list.html'
    )
    form = TrackForm
    fieldsets = (
        (_('Main'), {
            'fields': (
                'is_active',
                'name',
                'slug',
                'year',
                'file',
            )
        }),
        (_('Description'), {
            'fields': (
                'preview',
                'description',
            )
        }),
        (_('Image'), {
            'fields': (
                'image',
                '_large_preview',
            )
        }),
        (_('Created/Updated'), {
            'fields': (
                'created',
                'modified',
            )
        }),
    )
    list_display = (
        'name',
        'year',
        '_small_preview',
        'slug',
        'order',
    )
    readonly_fields = (
        'slug',
        'created',
        'modified',
        '_small_preview',
        '_large_preview',
    )
    inlines = (TrackFileInline,)
    change_actions = (
        'reset_slug',
    )
    changelist_actions = (
        'reset_slug',
        'sort_objects',
    )

    @takes_instance_or_queryset
    def reset_slug(self, request, qs):
        """Action to reset `slug` field for ``Track`` objects."""
        for obj in qs:
            obj.slug = None
            obj.save()

    reset_slug.label = _('Reset slug')

    def sort_objects(self, request, queryset):
        """Action to redirect to sorting page.

        This fix is needed to make ``DjangoObjectActions`` and
        ``SortableAdmin`` classes to work together with template from first
        class.

        """
        return HttpResponseRedirect('/admin/music/track/sort/')

    sort_objects.label = _('Sort objects')

    def _small_preview(self, obj):
        return image_preview(obj, size='small', field='image_thumbnail')

    _small_preview.short_description = _('Image preview')

    def _large_preview(self, obj):
        return image_preview(obj, size='large', field='image_thumbnail')

    _large_preview.short_description = _('Image preview')


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'file',
        'category',
        'created',
    )
