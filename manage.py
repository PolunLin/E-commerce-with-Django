#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
    site_packages = os.path.join(PROJECT_ROOT, 'libs')
    if site_packages not in sys.path:
        sys.path.insert(0, site_packages)
    sys.path.append(os.path.abspath(os.path.dirname(__file__)))
    sys.path.append('..')

    import dotenv
    dotenv.load_dotenv(os.path.join(os.path.dirname(PROJECT_ROOT), '.env'), True)
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
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
