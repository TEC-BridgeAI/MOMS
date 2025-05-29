# backend/create_hr_data.py
import os
import django
import random
from datetime import datetime, timedelta

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moms_project.settings')
django.setup()

# Import models
from django.contrib.auth.models import User
from apps.hr.models import Department, Employee

# Clear existing HR data
print("Clearing existing HR data...")
Employee.objects.all().delete()
Department.objects.all().delete()
print("Existing HR data cleared.")

# Create departments
departments = [
    {"name": "Engineering", "description": "Software development and IT operations"},
    {"name": "Marketing", "description": "Brand management and marketing campaigns"},
    {"name": "Sales", "description": "Customer acquisition and account management"},
    {"name": "Finance", "description": "Financial planning and accounting"},
    {"name": "HR", "description": "Recruitment and employee management"},
    {"name": "Operations", "description": "Day-to-day business operations"},
    {"name": "Research", "description": "Product research and development"}
]

for dept_data in departments:
    dept, created = Department.objects.get_or_create(
        name=dept_data["name"],
        defaults={'description': dept_data["description"]}
    )
    if created:
        print(f"Created department: {dept.name}")

# Create employees with realistic data
employees = [
    {"first_name": "John", "last_name": "Smith", "position": "Software Engineer", "department": "Engineering"},
    {"first_name": "Sarah", "last_name": "Johnson", "position": "Marketing Manager", "department": "Marketing"},
    {"first_name": "Michael", "last_name": "Williams", "position": "Sales Director", "department": "Sales"},
    {"first_name": "Emily", "last_name": "Brown", "position": "Financial Analyst", "department": "Finance"},
    {"first_name": "David", "last_name": "Jones", "position": "HR Specialist", "department": "HR"},
    {"first_name": "Jessica", "last_name": "Davis", "position": "Operations Manager", "department": "Operations"},
    {"first_name": "Robert", "last_name": "Miller", "position": "Research Scientist", "department": "Research"},
    {"first_name": "Jennifer", "last_name": "Wilson", "position": "Frontend Developer", "department": "Engineering"},
    {"first_name": "Thomas", "last_name": "Taylor", "position": "Backend Developer", "department": "Engineering"},
    {"first_name": "Lisa", "last_name": "Anderson", "position": "UX Designer", "department": "Engineering"},
    {"first_name": "James", "last_name": "Martinez", "position": "Sales Representative", "department": "Sales"},
    {"first_name": "Patricia", "last_name": "Garcia", "position": "Accountant", "department": "Finance"}
]

for i, emp_data in enumerate(employees):
    # Create user
    username = f"{emp_data['first_name'].lower()}.{emp_data['last_name'].lower()}"
    email = f"{username}@example.com"
    
    user, user_created = User.objects.get_or_create(
        username=username,
        defaults={
            'email': email,
            'first_name': emp_data['first_name'],
            'last_name': emp_data['last_name'],
            'password': 'password123'  # In production, use a secure password
        }
    )
    
    if user_created:
        user.set_password('password123')
        user.save()
        print(f"Created user: {username}")
    
    # Get department
    dept = Department.objects.get(name=emp_data['department'])
    
    # Create employee
    employee, emp_created = Employee.objects.get_or_create(
        user=user,
        defaults={
            'department': dept,
            'employee_id': f"EMP{1000+i}",
            'position': emp_data['position'],
            'hire_date': datetime.now().date() - timedelta(days=random.randint(30, 730)),
            'birth_date': datetime.now().date() - timedelta(days=random.randint(8000, 15000)),
            'phone_number': f"555-{random.randint(1000, 9999)}",
            'address': f"{random.randint(100, 999)} Main St, Anytown, USA"
        }
    )
    
    if emp_created:
        print(f"Created employee: {employee.user.first_name} {employee.user.last_name} ({employee.employee_id})")

print("HR sample data creation completed!")
