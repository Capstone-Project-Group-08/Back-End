"""
WSGI config for myproject3 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application # Django's function to create WSGI application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject3.settings')

# Create the WSGI application object that the web server uses to forward requests to Django
application = get_wsgi_application()
