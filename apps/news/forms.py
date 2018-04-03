from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import News


class NewsForm(forms.ModelForm):
    """Form for ``NewsAdmin`` class."""

    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'preview': CKEditorWidget(config_name='preview'),
            'full_text': CKEditorWidget(),
        }
