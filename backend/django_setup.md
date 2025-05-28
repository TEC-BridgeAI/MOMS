# Django Backend Setup

## Initial Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # macOS/Linux
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create Django project:
   ```bash
   django-admin startproject moms_project .
   ```

## Configure Settings

1. Create a settings directory:
   ```bash
   mkdir moms_project/settings
   ```

2. Create base settings file:
   ```python
   # moms_project/settings/base.py
   import os
   from pathlib import Path
   from dotenv import load_dotenv

   # Load environment variables
   load_dotenv()

   # Build paths inside the project
   BASE_DIR = Path(__file__).resolve().parent.parent.parent

   # Security settings
   SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-default-key-for-dev')
   DEBUG = os.getenv('DEBUG', 'True') == 'True'
   ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

   # Application definition
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       
       # Third-party apps
       'rest_framework',
       'corsheaders',
       'django_filters',
       
       # Local apps
       'apps.hr',
       'apps.analytics',
       'apps.automation',
       'apps.collaboration',
       'apps.compliance',
       'apps.crm',
       'apps.finance',
       'apps.project',
       'apps.strategy',
       'apps.supply_chain',
   ]

   MIDDLEWARE = [
       'django.middleware.security.SecurityMiddleware',
       'whitenoise.middleware.WhiteNoiseMiddleware',
       'django.contrib.sessions.middleware.SessionMiddleware',
       'corsheaders.middleware.CorsMiddleware',
       'django.middleware.common.CommonMiddleware',
       'django.middleware.csrf.CsrfViewMiddleware',
       'django.contrib.auth.middleware.AuthenticationMiddleware',
       'django.contrib.messages.middleware.MessageMiddleware',
       'django.middleware.clickjacking.XFrameOptionsMiddleware',
   ]

   ROOT_URLCONF = 'moms_project.urls'

   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [os.path.join(BASE_DIR, 'templates')],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]

   WSGI_APPLICATION = 'moms_project.wsgi.application'

   # Database
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': os.getenv('DB_NAME', 'moms_db'),
           'USER': os.getenv('DB_USER', 'postgres'),
           'PASSWORD': os.getenv('DB_PASSWORD', 'postgres'),
           'HOST': os.getenv('DB_HOST', 'localhost'),
           'PORT': os.getenv('DB_PORT', '5432'),
       }
   }

   # Password validation
   AUTH_PASSWORD_VALIDATORS = [
       {
           'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
       },
       {
           'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
       },
       {
           'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
       },
       {
           'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
       },
   ]

   # Internationalization
   LANGUAGE_CODE = 'en-us'
   TIME_ZONE = 'UTC'
   USE_I18N = True
   USE_TZ = True

   # Static files (CSS, JavaScript, Images)
   STATIC_URL = '/static/'
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

   # Media files
   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

   # Default primary key field type
   DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

   # REST Framework settings
   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': (
           'rest_framework_simplejwt.authentication.JWTAuthentication',
       ),
       'DEFAULT_PERMISSION_CLASSES': (
           'rest_framework.permissions.IsAuthenticated',
       ),
       'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
       'PAGE_SIZE': 10,
       'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
   }

   # CORS settings
   CORS_ALLOWED_ORIGINS = os.getenv('CORS_ORIGIN_WHITELIST', 'http://localhost:8080').split(',')
   ```

3. Create development settings:
   ```python
   # moms_project/settings/development.py
   from .base import *

   DEBUG = True

   # CORS settings for development
   CORS_ALLOW_ALL_ORIGINS = True

   # Email backend for development
   EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
   ```

4. Create production settings:
   ```python
   # moms_project/settings/production.py
   import os
   from .base import *

   DEBUG = False

   # Security settings
   SECURE_SSL_REDIRECT = True
   SESSION_COOKIE_SECURE = True
   CSRF_COOKIE_SECURE = True
   SECURE_BROWSER_XSS_FILTER = True
   SECURE_CONTENT_TYPE_NOSNIFF = True
   X_FRAME_OPTIONS = 'DENY'

   # AWS S3 settings for static and media files
   AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
   AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
   AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
   AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME', 'us-east-1')
   AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
   AWS_DEFAULT_ACL = 'public-read'
   AWS_S3_OBJECT_PARAMETERS = {
       'CacheControl': 'max-age=86400',
   }

   # Static and media files
   STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
   DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
   STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
   MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
   ```

5. Create `__init__.py` in settings directory:
   ```python
   # moms_project/settings/__init__.py
   import os

   # Default to development settings
   environment = os.getenv('DJANGO_ENVIRONMENT', 'development')

   if environment == 'production':
       from .production import *
   else:
       from .development import *
   ```

## Create App Modules

For each module (hr, analytics, etc.), create a Django app:

```bash
mkdir -p apps/hr
django-admin startapp hr apps/hr
```

Repeat for all modules.

## Configure URLs

1. Main URL configuration:
   ```python
   # moms_project/urls.py
   from django.contrib import admin
   from django.urls import path, include
   from django.conf import settings
   from django.conf.urls.static import static
   from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
       path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
       path('api/hr/', include('apps.hr.urls')),
       path('api/analytics/', include('apps.analytics.urls')),
       path('api/automation/', include('apps.automation.urls')),
       path('api/collaboration/', include('apps.collaboration.urls')),
       path('api/compliance/', include('apps.compliance.urls')),
       path('api/crm/', include('apps.crm.urls')),
       path('api/finance/', include('apps.finance.urls')),
       path('api/project/', include('apps.project.urls')),
       path('api/strategy/', include('apps.strategy.urls')),
       path('api/supply-chain/', include('apps.supply_chain.urls')),
   ]

   if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

## Create Models for Each Module

Example for HR module:

```python
# apps/hr/models.py
from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='employees')
    employee_id = models.CharField(max_length=20, unique=True)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    birth_date = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    emergency_contact = models.CharField(max_length=100, blank=True, null=True)
    emergency_phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.employee_id})"
```

## Create API Views

Example for HR module:

```python
# apps/hr/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Department, Employee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)
    
    class Meta:
        model = Employee
        fields = '__all__'
```

```python
# apps/hr/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['name']
    search_fields = ['name', 'description']

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['department', 'position', 'hire_date']
    search_fields = ['employee_id', 'user__first_name', 'user__last_name', 'position']
```

```python
# apps/hr/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

## Create Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Create Admin Interface

```python
# apps/hr/admin.py
from django.contrib import admin
from .models import Department, Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'get_full_name', 'department', 'position', 'hire_date')
    list_filter = ('department', 'hire_date')
    search_fields = ('employee_id', 'user__first_name', 'user__last_name', 'position')
    
    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_full_name.short_description = 'Name'
```

## Create Tests

```python
# apps/hr/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Department, Employee
import datetime

class DepartmentModelTest(TestCase):
    def setUp(self):
        Department.objects.create(name="Engineering", description="Software Engineering Department")
    
    def test_department_creation(self):
        department = Department.objects.get(name="Engineering")
        self.assertEqual(department.description, "Software Engineering Department")

class EmployeeModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="password123", 
                                        first_name="Test", last_name="User")
        department = Department.objects.create(name="Engineering")
        Employee.objects.create(
            user=user,
            department=department,
            employee_id="EMP001",
            position="Software Engineer",
            hire_date=datetime.date.today()
        )
    
    def test_employee_creation(self):
        employee = Employee.objects.get(employee_id="EMP001")
        self.assertEqual(employee.position, "Software Engineer")
        self.assertEqual(employee.user.first_name, "Test")
        self.assertEqual(employee.department.name, "Engineering")

class DepartmentAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.force_authenticate(user=self.user)
        self.department_data = {"name": "Marketing", "description": "Marketing Department"}
        self.department = Department.objects.create(name="Engineering", description="Engineering Department")
    
    def test_get_departments(self):
        response = self.client.get('/api/hr/departments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_create_department(self):
        response = self.client.post('/api/hr/departments/', self.department_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Department.objects.count(), 2)
```