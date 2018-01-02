from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AboutConfig(AppConfig):
    """Configuration for ``About`` app."""
    name = 'apps.about'
    verbose_name = _('About')
