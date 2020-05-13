from django.db import models
from django.utils.translation import ugettext_lazy as _


class News(models.Model):
    """Model for ``News`` page items.

    Attributes:
        title (str): News title.
        article (str): News article.
        published (datetime): Publication date.
        likes (int): Amount of likes.

    """
    title_ru = models.CharField(
        max_length=256,
        verbose_name=_('Russian title'),
    )
    title_en = models.CharField(
        max_length=256,
        verbose_name=_('English title'),
    )
    article_ru = models.TextField(
        verbose_name=_('Russian article'),
    )
    article_en = models.TextField(
        verbose_name=_('English article'),
    )
    published = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('Publication date')
    )
    likes = models.IntegerField(
        default=0,
        verbose_name=_('likes')
    )

    def inc_like(self):
        """Method to increment `likes` attribute."""
        self.likes += 1

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
