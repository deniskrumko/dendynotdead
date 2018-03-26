from django.db import models
from django.utils.translation import ugettext_lazy as _

from adminsortable.models import SortableMixin
from autoslug import AutoSlugField

from apps.core.models import BaseModel


class AboutInfo(SortableMixin, BaseModel):
    """Model for info block's on "About" page."""
    title = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_('title'),
    )
    slug = AutoSlugField(
        populate_from='title',
        unique_with=('title',),
        verbose_name=_('Slug'),
    )
    description = models.TextField(
        null=True,
        blank=False,
        verbose_name=_('description'),
    )
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True
    )

    def __str__(self):
        return self.title or '-'

    class Meta:
        verbose_name = _('Info')
        verbose_name_plural = _('Info')
        ordering = ('order',)
