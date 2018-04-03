from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from adminsortable.admin import SortableAdmin

from .forms import AboutInfoForm
from .models import AboutInfo


@admin.register(AboutInfo)
class AboutInfoAdmin(SortableAdmin):
    """Admin class for ``AboutInfo`` model."""
    form = AboutInfoForm
    fieldsets = (
        (_('Main'), {
            'fields': (
                'title',
                'slug',
                'description',
                'order',
            )
        }),
        (_('Created/Modified'), {
            'fields': (
                'created',
                'modified',
            )
        }),
    )
    list_display = (
        'title',
        'slug',
        'order',
    )
    readonly_fields = (
        'slug',
        'order',
        'created',
        'modified',
    )
