@echo off
REM Local development workflow script for Windows

REM Set environment variables
set DJANGO_SETTINGS_MODULE=moms_project.settings.development
set DEBUG=True
set SECRET_KEY=dev-secret-key-for-local-development-only

REM Activate virtual environment
call venv\Scripts\activate

REM Run database migrations
cd backend
python manage.py migrate

REM Start development server
python manage.py runserver

REM To deactivate the virtual environment when done
REM call deactivate