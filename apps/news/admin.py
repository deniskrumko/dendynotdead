from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from adminsortable.admin import SortableAdmin

from apps.core.admin import image_preview

from .forms import NewsForm
from .models import News


@admin.register(News)
class NewsAdmin(SortableAdmin, admin.ModelAdmin):
    """Admin class for ``News`` model."""
    form = NewsForm
    fieldsets = (
        (_('Main'), {
            'fields': (
                'is_active',
                'author',
                'title',
                'slug',
                'views',
                'order',
            )
        }),
        (_('Text'), {
            'fields': (
                'preview',
                'full_text',
            )
        }),
        (_('Image'), {
            'fields': (
                'image',
                'image_thumbnail',
                '_large_preview',
            )
        }),
        (_('Tracks'), {
            'fields': (
                'tracks',
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
        'slug',
        'title',
        'author',
        '_small_preview',
        'views',
        'created',
        'order',
    )
    readonly_fields = (
        'slug',
        'views',
        '_small_preview',
        '_large_preview',
        'created',
        'modified',
        'order',
    )

    def _small_preview(self, obj):
        return image_preview(obj, size='small', field='image_thumbnail')

    _small_preview.short_description = _('Image preview')

    def _large_preview(self, obj):
        return image_preview(obj, size='large', field='image_thumbnail')

    _large_preview.short_description = _('Image preview')
