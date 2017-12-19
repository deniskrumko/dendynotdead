from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoreConfig(AppConfig):
    """Configuration for ``Core`` app."""
    name = 'apps.core'
    app_label = _('Core')
