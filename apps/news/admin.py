from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from adminsortable.admin import SortableAdmin

from .models import News
from .forms import NewsForm
from apps.core.admin import small_preview, large_preview


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
        return small_preview(obj)

    _small_preview.short_description = _('Image preview')

    def _large_preview(self, obj):
        return large_preview(obj)

    _large_preview.short_description = _('Image preview')
