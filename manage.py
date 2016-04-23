#!/usr/bin/env python
import os
import sys

from  utility.utils import  ENV_MODE



if __name__ == "__main__":

    if ENV_MODE == 'dev' or ENV_MODE == 'development':
         os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{project_name|lower}}.settings.development")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{project_name|lower}}.settings.production")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
