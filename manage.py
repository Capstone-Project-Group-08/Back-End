#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os # Used to interact with the operating system
import sys # Used to work with command-line arguments


def main():
    """Run administrative tasks."""

    # Setting the default settings module for the Django project
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject3.settings')
    try:
        # Importing Django's command-line execution utility
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Handles the error if Django is not installed or misconfigured
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Executes the command-line arguments passed to the script
    execute_from_command_line(sys.argv)

# Ensures the main function runs only when this file is executed directly
if __name__ == '__main__':
    main()
