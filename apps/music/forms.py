from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import Track


class TrackForm(forms.ModelForm):
    """Form for ``TrackAdmin`` class."""

    class Meta:
        model = Track
        fields = '__all__'
        widgets = {
            'preview': CKEditorWidget(config_name='preview'),
            'description': CKEditorWidget(),
        }
