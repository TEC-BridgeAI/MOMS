# Getting Started with MOMS Project

This guide will help you set up and start developing the MOMS (Modular Organizational Management System) project.

## Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL 13+
- Git
- Docker and Docker Compose (optional, for containerized development)

## Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/moms.git
cd moms
```

## Step 2: Backend Setup

### Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

```bash
# Copy example env file
cp .env.example .env

# Edit .env with your configuration
# Especially database connection details
```

### Initialize Django Project

```bash
# Create Django project structure
django-admin startproject moms_project backend

# Create app modules
cd backend
python manage.py startapp hr apps/hr
python manage.py startapp analytics apps/analytics
python manage.py startapp automation apps/automation
python manage.py startapp collaboration apps/collaboration
python manage.py startapp compliance apps/compliance
python manage.py startapp crm apps/crm
python manage.py startapp finance apps/finance
python manage.py startapp project apps/project
python manage.py startapp strategy apps/strategy
python manage.py startapp supply_chain apps/supply_chain
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Development Server

```bash
python manage.py runserver
```

## Step 3: Frontend Setup

### Install Dependencies

```bash
cd frontend
npm install
```

### Run Development Server

```bash
npm run serve
```

## Step 4: Access the Application

- Backend API: http://localhost:8000/api/
- Admin interface: http://localhost:8000/admin/
- Frontend: http://localhost:8080/

## Development Workflow

1. Create models in Django apps
2. Create serializers and API views
3. Implement frontend components and views
4. Test functionality
5. Commit changes to Git

## Using Docker (Optional)

If you prefer to use Docker for development:

```bash
# Start all services
docker-compose -f deployment/docker/docker-compose.yml up -d

# View logs
docker-compose -f deployment/docker/docker-compose.yml logs -f

# Stop all services
docker-compose -f deployment/docker/docker-compose.yml down
```

## Module Development

Each module should follow this structure:

1. **Backend**:
   - Models in `apps/module_name/models.py`
   - Serializers in `apps/module_name/serializers.py`
   - Views in `apps/module_name/views.py`
   - URLs in `apps/module_name/urls.py`
   - Tests in `apps/module_name/tests.py`

2. **Frontend**:
   - Components in `frontend/src/components/module_name/`
   - Views in `frontend/src/views/module_name/`
   - Store module in `frontend/src/store/modules/module_name.js`
   - API service in `frontend/src/services/module_name.service.js`

## AWS Deployment

To deploy to AWS:

1. Set up AWS CLI and configure credentials
2. Update environment variables in `.env`
3. Run deployment script:

```bash
chmod +x deployment/aws/scripts/deploy.sh
./deployment/aws/scripts/deploy.sh
```

For more detailed instructions, see the [development_procedure.md](development_procedure.md) file.