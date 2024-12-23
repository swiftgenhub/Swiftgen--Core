#!/usr/bin/env python
import os
import sys

def main():
    """Run administrative tasks."""
    try:
        # Determine the environment and set the corresponding settings module
        env = os.getenv('DJANGO_ENV', 'production').lower()
        
        if env == 'production':
            settings_module = 'Work.settings.production'
        elif env == 'staging':
            settings_module = 'Work.settings.staging'
        else:
            settings_module = 'Work.settings.development'
        
        # Ensure the settings module is correctly set
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
        
        # Execute Django management commands
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)

    except ImportError as exc:
        # Handle missing Django or dependencies
        raise ImportError(
            "Couldn't import Django. Ensure it's installed and available on your PYTHONPATH. "
            "Did you activate the virtual environment?"
        ) from exc
    except Exception as e:
        # Handle other unforeseen errors
        sys.stderr.write(f"An error occurred: {str(e)}\n")
        sys.exit(1)

if __name__ == '__main__':
    main()
