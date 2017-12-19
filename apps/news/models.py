from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.core.models import BaseModel
from apps.users.models import User


class News(BaseModel):
    """Documentation"""
    author = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name='news',
        verbose_name=_('Author'),
        on_delete=models.SET_NULL
    )
    title = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_('Title'),
    )
    content = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Content'),
    )
    image = models.ImageField(
        null=True,
        blank=True,
        verbose_name=_('Image'),
        upload_to=BaseModel.file_upload_path
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
