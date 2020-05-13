import factory

from .models import News


class NewsFactory(factory.DjangoModelFactory):
    """Factory for ``News`` model."""
    class Meta:
        model = News

    title = factory.Faker('word')
    article = factory.Faker('text')
