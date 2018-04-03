from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import AboutInfo


class AboutInfoForm(forms.ModelForm):
    """Form for ``AboutInfoAdmin`` class."""

    class Meta:
        model = AboutInfo
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
        }
