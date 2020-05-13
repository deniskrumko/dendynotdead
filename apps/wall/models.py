from django.db import models
from django.utils.translation import ugettext_lazy as _


class WallMessage(models.Model):
    """Model for ``The Wall`` page messages.

    Attributes:
        message (str): Message on the wall.
        published (datetime): Publication date.
        session_id (str): ID of the session.

    """
    message = models.CharField(
        max_length=128,
        verbose_name=_('Message'),
    )
    published = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('Publication date'),
        auto_now=True,
    )
    session_id = models.CharField(
        max_length=512,
        verbose_name=_('Session ID'),
    )
