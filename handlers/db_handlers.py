import os
import sys
import django
import subprocess
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Add the project directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moms_project.settings.serverless')
django.setup()

def run_migrations(event, context):
    """
    Run Django migrations on deployment
    """
    try:
        logger.info("Starting database migrations")
        from django.core.management import call_command
        call_command('migrate')
        logger.info("Migrations completed successfully")
        return {
            'statusCode': 200,
            'body': 'Migrations completed successfully'
        }
    except Exception as e:
        logger.error(f"Migration error: {str(e)}")
        return {
            'statusCode': 500,
            'body': f'Migration error: {str(e)}'
        }