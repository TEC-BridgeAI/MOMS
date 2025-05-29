import os

# Default to development settings
environment = os.getenv('DJANGO_ENVIRONMENT', 'development')

if environment == 'production':
    from .production import *
elif environment == 'serverless':
    from .serverless import *
else:
    from .development import *