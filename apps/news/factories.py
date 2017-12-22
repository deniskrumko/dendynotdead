import factory

from .models import News


class NewsFactory(factory.DjangoModelFactory):
    """Factory for ``News`` model."""
    title = factory.Faker('name')
    preview = factory.Faker('sentence')
    full_text = factory.Faker('text')

    class Meta:
        model = News
