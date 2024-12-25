#!/usr/bin/env python
import os
import sys

def main():
    """Run administrative tasks."""
    try:
        # Get the environment type and set the corresponding settings module
        env = os.getenv('DJANGO_ENV', 'production').lower()
        
        if env == 'production':
            settings_module = 'Work.settings.production'
        elif env == 'staging':
            settings_module = 'Work.settings.staging'
        elif env == 'development':
            settings_module = 'Work.settings.development'
        else:
            raise ValueError(f"Unknown DJANGO_ENV value: {env}")

        # Set the settings module for Django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

        # Run Django management commands
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
    
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Ensure it's installed and available on your PYTHONPATH. "
            "Did you activate your virtual environment?"
        ) from exc
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)

if __name__ == '__main__':
    main()
