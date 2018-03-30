from django import forms

from .models import AboutInfo
from ckeditor.widgets import CKEditorWidget


class AboutInfoForm(forms.ModelForm):
    """Form for ``AboutInfoAdmin`` class."""

    class Meta:
        model = AboutInfo
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
        }
