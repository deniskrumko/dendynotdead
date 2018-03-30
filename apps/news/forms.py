from django import forms

from .models import News
from ckeditor.widgets import CKEditorWidget


class NewsForm(forms.ModelForm):
    """Form for ``NewsAdmin`` class."""

    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'preview': CKEditorWidget(config_name='preview'),
            'full_text': CKEditorWidget(),
        }
