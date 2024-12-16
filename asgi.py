"""
ASGI config for myproject3 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os # Standard library module to interact with the operating system

from django.core.asgi import get_asgi_application # Function to get the ASGI application for Django
# Set the default settings module for the 'myproject3' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject3.settings')

application = get_asgi_application()
