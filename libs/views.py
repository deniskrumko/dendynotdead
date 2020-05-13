from django.http import HttpResponseRedirect
from django.utils import translation


class BaseViewMixin(object):
    """Base mixin for views."""
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # context['lang'] = request.session.get('django_language', 'ru')
        # Add prefix 'js/' to all Javascript imports
        if hasattr(self, 'import_js'):
            context['import_js'] = [
                'js/{0}'.format(js) for js in self.import_js
            ]

        # Add prefix 'css/' to all CSS imports
        if hasattr(self, 'import_css'):
            context['import_css'] = [
                'css/{0}'.format(css) for css in self.import_css
            ]

        # Add title of the page
        context['title_name'] = self.title

        # Add current section for Menu
        context['menu_section'] = self.menu_section
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):

        return HttpResponseRedirect(request.path)
