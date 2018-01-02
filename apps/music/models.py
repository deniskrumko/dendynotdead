from apps.core.models import BaseModel
from django.utils.translation import ugettext_lazy as _
from django.db import models
from autoslug import AutoSlugField


class File(BaseModel):
    CATEGORIES = (
        ('music', 'Music'),
        ('gtp', 'Guitar PRO'),
        ('text', 'Text'),
        ('video', 'Video'),
    )
    name = models.CharField(
        null=True,
        blank=False,
        max_length=255,
        verbose_name=_('Name')
    )
    file = models.FileField(
        null=True,
        blank=False,
        upload_to=BaseModel.file_upload_path,
        verbose_name=_('File')
    )
    category = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices=CATEGORIES,
        default=CATEGORIES[0][0],
        verbose_name=_('Category'),
    )

    @property
    def url(self):
        return self.file.url if self.file else None

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('File')
        verbose_name_plural = _('Files')


class Track(BaseModel):
    """Documentation"""
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Is active'),
    )
    name = models.CharField(
        null=True,
        blank=False,
        max_length=255,
        verbose_name=_('Name')
    )
    year = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_('Year'),
    )
    slug = AutoSlugField(
        populate_from='name',
        unique_with=('name',),
        verbose_name=_('Slug'),
    )
    file = models.ForeignKey(
        File,
        null=True,
        blank=False,
        related_name='tracks',
        verbose_name=_('File'),
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to=BaseModel.file_upload_path,
        verbose_name=_('Image')
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
    )

    def truncated_description(self):
        truncate_lenght = 250

        if len(self.description) < truncate_lenght:
            return self.description

        return self.description[:truncate_lenght] + '...'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Track')
        verbose_name_plural = _('Tracks')
        ordering = ('-year', 'name')


class TrackFile(models.Model):
    """Documentation"""
    track = models.ForeignKey(
        Track,
        null=True,
        blank=False,
        related_name='extra_files',
        verbose_name=_('Track'),
    )
    file = models.ForeignKey(
        File,
        null=True,
        blank=False,
        related_name='related_tracks',
        verbose_name=_('File'),
    )
    sort_order = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Sort order')
    )

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = _('Track File')
        verbose_name_plural = _('Track Files')
        ordering = ('sort_order',)
