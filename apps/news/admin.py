from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from .models import News
from adminsortable.admin import SortableAdmin


@admin.register(News)
class NewsAdmin(SortableAdmin, admin.ModelAdmin):
    """Admin class for ``News`` model."""
    list_display = (
        'slug',
        'title',
        'author',
        '_image',
        'views',
        'created',
        'order',
    )
    readonly_fields = (
        'views',
    )

    def _image(self, obj):
        return mark_safe(
            f'<img src="{obj.image.url}" style="height: 28px;">'
        ) if obj.image else '-'

    _image.short_description = _('Image preview')
