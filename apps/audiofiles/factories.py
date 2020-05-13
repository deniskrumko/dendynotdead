import factory

from .models import AudioFile, AudioTrack


class AudioTrackFactory(factory.DjangoModelFactory):
    """Factory for ``AudioTrack`` model."""
    class Meta:
        model = AudioTrack

    artist = 'Dendy Not Dead'
    track_name = factory.Faker('word')


class AudioFileFactory(factory.DjangoModelFactory):
    """Factory for ``AudioFile`` model."""
    class Meta:
        model = AudioFile

    file_mp3 = factory.Faker('url')
    file_ogg = factory.Faker('url')
    file_wav = factory.Faker('url')
    parent_track = factory.SubFactory(AudioTrackFactory)
