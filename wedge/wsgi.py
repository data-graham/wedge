import os, sys
from django.core.wsgi import get_wsgi_application


def application(environ, start_response):
    return get_wsgi_application()(environ, start_response)
