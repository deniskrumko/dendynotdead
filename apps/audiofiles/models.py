from datetime import datetime

from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from . import AUDIO_VERSION


class AudioFile(models.Model):
    file_mp3 = models.URLField(
        blank=True,
        max_length=256,
        verbose_name=_('Audio File URL (MP3)'),
    )
    file_ogg = models.URLField(
        blank=True,
        max_length=256,
        verbose_name=_('Audio File URL (OGG)'),
    )
    file_wav = models.URLField(
        blank=True,
        max_length=256,
        verbose_name=_('Audio File URL (WAV)'),
    )
    version = models.CharField(
        max_length=3,
        choices=AUDIO_VERSION,
        default=AUDIO_VERSION[0],
        verbose_name=_('Audio Type'),
    )
    main_priority = models.BooleanField(
        default=False,
        verbose_name=_('Main priority')
    )
    parent_track = models.ForeignKey(
        null=True,
        to='AudioTrack',
        verbose_name=_('Related Audio Track'),
    )

    def __str__(self):
        return '{0} ({1})'.format(
            self.parent_track.track_name,
            self.version
        )

    def clean(self):
        """Custom clean method."""
        files = (self.file_ogg, self.file_wav, self.file_mp3)
        if not any(files):
            raise ValidationError(_(
                'At least one of the files should be uploaded'
            ))


class AudioTrack(models.Model):
    artist = models.CharField(
        max_length=128,
        default=_('Dendy Not Dead'),
        verbose_name=_('Artist'),
    )
    track_name = models.CharField(
        max_length=256,
        verbose_name=_('Track Name'),
    )
    description_ru = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Russian description'),
    )
    description_en = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('English description'),
    )
    lyrics = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Lyrics'),
    )
    published = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('Publication date')
    )
    gtp_file = models.FileField(
        null=True,
        blank=True,
        verbose_name=_('GuitarPro File'),
        upload_to='gtp'
    )
    youtube_link = models.URLField(
        null=True,
        blank=True,
        verbose_name=_('YouTube link')
    )
    likes = models.IntegerField(
        default=0,
        verbose_name=_('likes')
    )

    def inc_like(self):
        """Method to increment `likes` attribute."""
        self.likes += 1

    @property
    def was_published(self):
        """Property to get message - when track was published."""
        delta = (datetime.now().date() - self.published).days
        if delta == 0:
            return _('This track was published today!')
        else:
            return _('This track was published {0} days ago'.format(delta))

    @property
    def brand_new_track(self):
        """Property to check is brand new."""
        delta = (datetime.now().date() - self.published).days
        if delta < settings.BRAND_NEW_TRACK_DAYS:
            return True

    @property
    def short_name(self):
        """Property to get short name of track."""
        if len(self.track_name) > 25:
            return self.track_name[:25] + '...'
        else:
            return self.track_name

    def __str__(self):
        """String representation of audio track."""
        return '{0} — {1}'.format(self.artist, self.track_name)
