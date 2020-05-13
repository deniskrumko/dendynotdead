from django.views.generic.base import TemplateView

from libs.views import BaseViewMixin


class IndexView(BaseViewMixin, TemplateView):
    template_name = 'index.html'
    title = 'DendyNotDead'
    menu_section = 'index'
    import_js = ('detect.min.js', 'index.js', 'base.js')
    import_css = ('index.css', 'csshake.min.css')


class AboutView(BaseViewMixin, TemplateView):
    template_name = 'about.html'
    title = 'DendyNotDead'
    menu_section = 'about'
    import_js = ('base.js', 'about.js')
    import_css = (
        'about.css', 'body.css', 'menu.css', 'logo.css', 'shortcuts.css'
    )
