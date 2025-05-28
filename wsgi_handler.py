import os
import sys

# Add the project directory to the sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moms_project.settings.serverless')

# Import the WSGI application
from moms_project.wsgi import application

# Handler for API Gateway
def handler(event, context):
    return application(event, context)