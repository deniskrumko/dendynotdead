from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SearchConfig(AppConfig):
    """Configuration for ``DendyNotDead`` app."""
    name = 'apps.search'
    verbose_name = _('Search')