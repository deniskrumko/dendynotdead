from django.contrib import admin

from .models import WallMessage


@admin.register(WallMessage)
class WallAdmin(admin.ModelAdmin):
    """Admin class for ``WallMessage`` model."""
    list_display = (
        'id', 'message', 'published'
    )
