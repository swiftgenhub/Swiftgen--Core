#!/usr/bin/env python
import os
import sys

def main():
    """Run administrative tasks."""
    # Determine the environment and set the corresponding settings module
    env = os.getenv('DJANGO_ENV', 'production').lower()
    
    if env == 'production':
        settings_module = 'Work.settings.production'
    elif env == 'staging':
        settings_module = 'Work.settings.staging'
    else:
        settings_module = 'Work.settings.development'
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    
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
