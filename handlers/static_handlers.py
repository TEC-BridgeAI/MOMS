import os
import sys
import django
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Add the project directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moms_project.settings.serverless')
django.setup()

def collect_static(event, context):
    """
    Collect static files and upload to S3
    """
    try:
        logger.info("Starting static file collection")
        from django.core.management import call_command
        call_command('collectstatic', '--noinput')
        logger.info("Static files collected successfully")
        return {
            'statusCode': 200,
            'body': 'Static files collected successfully'
        }
    except Exception as e:
        logger.error(f"Static collection error: {str(e)}")
        return {
            'statusCode': 500,
            'body': f'Static collection error: {str(e)}'
        }