from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class NewsConfig(AppConfig):
    """Configuration for ``News`` app."""
    name = 'apps.news'
    app_label = _('News')
