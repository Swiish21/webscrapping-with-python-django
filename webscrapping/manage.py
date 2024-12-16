#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

"""

This is the `main` function in a Django project's `manage.py` file. It sets the `DJANGO_SETTINGS_MODULE` environment variable to point to the project's settings file (`webscrapping.settings`) and then attempts to import and run Django's management commands from the command line. If Django is not installed or not found, it raises an `ImportError` with a helpful error message.

"""
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webscrapping.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
