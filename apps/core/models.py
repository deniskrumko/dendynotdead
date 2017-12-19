from uuid import uuid4

from django_extensions.db.models import TimeStampedModel


class BaseModel(TimeStampedModel):
    """Base model."""

    class Meta:
        abstract = True

    @classmethod
    def file_upload_path(cls, instance, filename):
        """Default file upload handler."""
        folder = instance._meta.model_name.replace(' ', '-')
        extension = filename.split('.')[-1]
        return f'{folder}/{uuid4()}.{extension}'
