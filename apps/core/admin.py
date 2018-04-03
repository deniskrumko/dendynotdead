from django.utils.safestring import mark_safe


def image_preview(obj, size, field='image',):
    assert size in ('small', 'large')

    image_field = getattr(obj, field)
    return mark_safe(
        f'<img src="{image_field.url}" class="{size}-preview">'
    ) if image_field else '-'
