import factory

from .models import Track


class TrackFactory(factory.DjangoModelFactory):
    """Factory for ``Track`` model."""
    name = factory.sequence(lambda x: 'Name %d' % x)
    year = 2018

    class Meta:
        model = Track
