from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from adminsortable.models import SortableMixin
from autoslug import AutoSlugField

from apps.core.models import BaseModel
from apps.music.models import Track
from apps.users.models import User


class News(SortableMixin, BaseModel):
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
    tracks = models.ManyToManyField(
        to=Track,
        blank=True,
        related_name='news',
        verbose_name=_('Tracks'),
    )
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
        ordering = ('-order',)

    def increment_view(self):
        self.views += 1
        self.save()

    @property
    def when(self):
        difference = timezone.now() - self.created

        if difference.days:
            if difference.days <= 7:
                suffix = 'дней назад'

                if difference.days == 1:
                    suffix = 'день назад'
                elif difference.days in [2, 3, 4]:
                    suffix = 'дня назад'

                return f'{difference.days} {suffix}'
            else:
                return self.created

        hours = difference.seconds // 60 // 60

        if hours:
            suffix = 'часов назад'
            if hours % 10 == 1 and hours != 11:
                suffix = 'час назад'
            if hours % 10 in [2, 3, 4] and hours not in [12, 13, 14]:
                suffix = 'часа назад'
            return f'{hours} {suffix}'

        minutes = difference.seconds // 60

        if minutes:
            suffix = 'минут назад'
            if minutes % 10 == 1 and minutes != 11:
                suffix = 'минуту назад'
            if minutes % 10 in [2, 3, 4] and minutes not in [12, 13, 14]:
                suffix = 'минуты назад'

            return f'{minutes} {suffix}'

        return 'Только что'
