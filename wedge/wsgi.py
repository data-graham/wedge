"""
WSGI config for thinkpackage project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys
from django.core.wsgi import get_wsgi_application


def application(environ, start_response):
    return get_wsgi_application()(environ, start_response)
