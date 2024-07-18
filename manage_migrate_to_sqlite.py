#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Refranes.settings_migrate_to_sqlite')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

# Script 
#    try:
#       exec(open("migrate_mysql_to_sqlite.py").read())
#    except:
#       print("Ha ocurrido un error en migrate_mysql_to_sqlite.py")
#    else:
#       print("Ejecución correcta de migrate_mysql_to_sqlite.py")

if __name__ == '__main__':
    main()
