from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from adminsortable.admin import SortableAdmin
from django_object_actions import DjangoObjectActions, takes_instance_or_queryset
from .forms import AboutInfoForm
from .models import AboutInfo
from django.http.response import HttpResponseRedirect


@admin.register(AboutInfo)
class AboutInfoAdmin(DjangoObjectActions, SortableAdmin):
    """Admin class for ``AboutInfo`` model."""
    sortable_change_list_with_sort_link_template = (
        'django_object_actions/change_list.html'
    )
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
    change_actions = (
        'on_site',
    )
    changelist_actions = (
        'on_site',
    )

    @takes_instance_or_queryset
    def on_site(self, request, qs=None):
        """Method to view tracks or one track on site."""
        if qs.count() > 1:
            return HttpResponseRedirect('/about/')

        about_info = qs.first()
        return HttpResponseRedirect(f'/about/#{about_info.slug}')

    on_site.label = _('View on site')
