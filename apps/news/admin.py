from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """Admin for ``News`` model."""
    list_display = (
        'id', 'title_ru', 'published'
    )
    readonly_fields = ('likes',)
    fieldsets = (
        ('Russian', {
            'fields': (
                'title_ru',
                'article_ru',
            )
        }),
        ('English', {
            'fields': (
                'title_en',
                'article_en',
            )
        }),
        ('Info', {
            'fields': (
                'published',
                'likes'
            )
        }),
    )
