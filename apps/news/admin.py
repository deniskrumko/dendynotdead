from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.http.response import HttpResponseRedirect
from adminsortable.admin import SortableAdmin
from django_object_actions import DjangoObjectActions, takes_instance_or_queryset
from apps.core.admin import image_preview

from .forms import NewsForm
from .models import News


@admin.register(News)
class NewsAdmin(DjangoObjectActions, SortableAdmin):
    """Admin class for ``News`` model."""
    sortable_change_list_with_sort_link_template = (
        'django_object_actions/change_list.html'
    )
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
    change_actions = (
        'on_site',
    )
    changelist_actions = (
        'on_site',
    )

    @takes_instance_or_queryset
    def on_site(self, request, qs=None):
        """Method to view all news or one news on site."""
        if qs.count() != 1:
            return HttpResponseRedirect('/news/')

        news = qs.first()
        return HttpResponseRedirect(f'/news/{news.slug}/')

    on_site.label = _('View on site')

    def _small_preview(self, obj):
        return image_preview(obj, size='small', field='image_thumbnail')

    _small_preview.short_description = _('Image preview')

    def _large_preview(self, obj):
        return image_preview(obj, size='large', field='image_thumbnail')

    _large_preview.short_description = _('Image preview')
