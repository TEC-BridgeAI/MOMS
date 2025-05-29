"""
ASGI config for moms_project project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moms_project.settings')

application = get_asgi_application()