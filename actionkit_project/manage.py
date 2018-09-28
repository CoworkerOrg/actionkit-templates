#!/usr/bin/env python
import os
import sys

def serve_templates():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "actionkit_app.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    serve_templates()
