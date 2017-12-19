from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.core.models import BaseModel
from apps.users.models import User
from autoslug import AutoSlugField


class News(BaseModel):
    """Documentation"""
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Is active'),
    )
    author = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name='news_author',
        verbose_name=_('Author'),
        on_delete=models.SET_NULL
    )
    title = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_('Title'),
    )
    slug = AutoSlugField(
        populate_from='title',
        verbose_name=_('Slug'),
        unique_with=('title',)
    )
    preview = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Preview'),
    )
    full_text = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Full text'),
    )
    image = models.ImageField(
        null=True,
        blank=True,
        verbose_name=_('Image'),
        upload_to=BaseModel.file_upload_path
    )
    views = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Views')
    )
    likes = models.ManyToManyField(
        User,
        blank=True,
        related_name='news_likes',
        verbose_name=_('Likes')
    )

    def __str__(self):
        return self.title

    @property
    def likes_count(self):
        return self.likes.count()

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
