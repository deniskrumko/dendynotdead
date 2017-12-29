from django.shortcuts import render_to_response
from django.template import RequestContext


def handler404(request):
    response = render_to_response('errors/404.html')
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('errors/500.html')
    response.status_code = 500
    return response
