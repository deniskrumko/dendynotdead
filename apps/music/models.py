from django.db import models
from django.utils.translation import ugettext_lazy as _

from adminsortable.models import SortableMixin
from autoslug import AutoSlugField

from apps.core.models import BaseModel


class File(BaseModel):
    """Model for storing files in specified categories.

    Attributes:
        name (str): name of file.
        file (File): file itself.
        category (str): category of file.

    """
    CATEGORIES = (
        ('music', 'Music'),
        ('demo', 'Demo'),
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
    obfuscate_filename = models.BooleanField(
        default=True,
        verbose_name=_('Obfuscate filename'),
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
        """Shortcut to get file URL."""
        return self.file.url if self.file else None

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('File')
        verbose_name_plural = _('Files')


class Track(SortableMixin, BaseModel):
    """Model for storing track's information.

    Attributes:
        is_active (bool): display track on site or not.
        name (str): name of track.
        year (int): year, when track was created.
        slug (str): slug from track name.
        file (File): related ``File`` model.
        image (File): image file.
        description (str): track description.

    """
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
        blank=True,
        related_name='tracks',
        verbose_name=_('File'),
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to=BaseModel.file_upload_path,
        verbose_name=_('Image')
    )
    preview = models.TextField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Preview'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
    )
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Track')
        verbose_name_plural = _('Tracks')
        ordering = ('-order',)

    def save(self, *args, **kwargs):
        if not self.id:
            self.order = 0

        super().save(*args, **kwargs)


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
