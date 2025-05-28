#!/bin/bash
# Local development workflow script for macOS/Linux

# Set environment variables
export DJANGO_SETTINGS_MODULE=moms_project.settings.development
export DEBUG=True
export SECRET_KEY=dev-secret-key-for-local-development-only

# Activate virtual environment
source venv/bin/activate

# Run database migrations
cd backend
python manage.py migrate

# Start development server
python manage.py runserver

# To deactivate the virtual environment when done
# deactivate