from uuid import uuid4

from django_extensions.db.models import TimeStampedModel


class BaseModel(TimeStampedModel):
    """Base model."""

    class Meta:
        abstract = True

    @classmethod
    def file_upload_path(cls, instance, filename):
        """Default file upload handler.

        If model has `obfuscate_filename` field and it's True for instance,
        then filename will be replaced with UUID4. If it's False - file will
        be saved with original name.

        If model has no `obfuscate_filename` field - file name will be
        obfuscated anyway. That's the rule, guys.

        """
        if hasattr(instance, 'obfuscate_filename'):
            if not instance.obfuscate_filename:
                folder = instance._meta.model_name.replace(' ', '-')
                return f'{folder}/{filename}'

        folder = instance._meta.model_name.replace(' ', '-')
        extension = filename.split('.')[-1]
        return f'{folder}/{uuid4()}.{extension}'
