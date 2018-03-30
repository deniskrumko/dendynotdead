from django.utils.safestring import mark_safe


def small_preview(obj):
    return mark_safe(
        f'<img src="{obj.image.url}" class="small-preview">'
    ) if obj.image else '-'


def large_preview(obj):
    return mark_safe(
        f'<img src="{obj.image.url}" class="large-preview">'
    ) if obj.image else '-'
