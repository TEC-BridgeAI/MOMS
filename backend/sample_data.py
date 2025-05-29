# backend/sample_data.py
import os
import django
import random
from datetime import datetime, timedelta
from decimal import Decimal

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moms_project.settings')
django.setup()

# Import models
from django.contrib.auth.models import User
from apps.hr.models import Department, Employee
from apps.crm.models import Customer, Contact, Opportunity
from apps.project.models import Project, Task
from apps.finance.models import Account, Invoice
from apps.supply_chain.models import Supplier, Product

# Create superuser if it doesn't exist
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Created superuser: admin/admin123")

# Create regular users
users = []
for i in range(1, 6):
    username = f"user{i}"
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(
            username=username,
            email=f"user{i}@example.com",
            password="password123",
            first_name=f"User{i}",
            last_name=f"Test"
        )
        users.append(user)
        print(f"Created user: {username}")
    else:
        users.append(User.objects.get(username=username))

# Create HR data
departments = ["Engineering", "Marketing", "Sales", "Finance", "HR"]
for dept_name in departments:
    dept, created = Department.objects.get_or_create(
        name=dept_name,
        defaults={'description': f"{dept_name} department"}
    )
    if created:
        print(f"Created department: {dept_name}")

# Create employees
for i, user in enumerate(users):
    dept = Department.objects.all()[i % len(departments)]
    employee, created = Employee.objects.get_or_create(
        user=user,
        defaults={
            'department': dept,
            'employee_id': f"EMP{1000+i}",
            'position': random.choice(["Manager", "Specialist", "Coordinator", "Analyst", "Director"]),
            'hire_date': datetime.now().date() - timedelta(days=random.randint(30, 365))
        }
    )
    if created:
        print(f"Created employee: {employee.employee_id}")

# Create CRM data
company_names = ["Acme Corp", "Globex", "Initech", "Umbrella Corp", "Stark Industries"]
for name in company_names:
    customer, created = Customer.objects.get_or_create(
        name=name,
        defaults={
            'customer_type': 'company',
            'email': f"info@{name.lower().replace(' ', '')}.com",
            'phone': f"555-{random.randint(1000, 9999)}",
            'created_by': random.choice(users)
        }
    )
    if created:
        print(f"Created customer: {name}")
        
        # Create contacts for this customer
        Contact.objects.create(
            customer=customer,
            first_name=random.choice(["John", "Jane", "Michael", "Sarah", "David"]),
            last_name=random.choice(["Smith", "Johnson", "Williams", "Brown", "Jones"]),
            position="CEO",
            email=f"ceo@{name.lower().replace(' ', '')}.com",
            is_primary=True
        )
        
        # Create opportunities
        Opportunity.objects.create(
            name=f"{name} Project",
            customer=customer,
            amount=Decimal(random.randint(10000, 100000)),
            status=random.choice(['new', 'qualified', 'proposal', 'negotiation']),
            expected_close_date=datetime.now().date() + timedelta(days=random.randint(30, 90)),
            created_by=random.choice(users)
        )

# Create Project data
for i in range(5):
    project, created = Project.objects.get_or_create(
        name=f"Project {i+1}",
        defaults={
            'description': f"Description for Project {i+1}",
            'status': random.choice(['planning', 'active', 'on_hold', 'completed']),
            'start_date': datetime.now().date() - timedelta(days=random.randint(0, 30)),
            'end_date': datetime.now().date() + timedelta(days=random.randint(30, 90)),
            'manager': random.choice(users),
            'created_by': random.choice(users)
        }
    )
    if created:
        print(f"Created project: {project.name}")
        project.members.add(*random.sample(list(users), k=random.randint(1, 3)))
        
        # Create tasks for this project
        for j in range(3):
            Task.objects.create(
                project=project,
                title=f"Task {j+1} for {project.name}",
                description=f"Description for Task {j+1}",
                priority=random.choice(['low', 'medium', 'high']),
                status=random.choice(['todo', 'in_progress', 'review', 'done']),
                assigned_to=random.choice(users),
                due_date=datetime.now().date() + timedelta(days=random.randint(1, 30)),
                created_by=random.choice(users)
            )

# Create Finance data
account_types = ['asset', 'liability', 'equity', 'revenue', 'expense']
for i, account_type in enumerate(account_types):
    Account.objects.get_or_create(
        name=f"{account_type.capitalize()} Account",
        defaults={
            'code': f"{account_type[0].upper()}{1000+i}",
            'account_type': account_type,
            'description': f"Main {account_type} account"
        }
    )

# Create Supply Chain data
supplier_names = ["Supplier A", "Supplier B", "Supplier C", "Supplier D", "Supplier E"]
for name in supplier_names:
    supplier, created = Supplier.objects.get_or_create(
        name=name,
        defaults={
            'contact_name': f"{random.choice(['John', 'Jane', 'Michael'])} {random.choice(['Smith', 'Johnson', 'Brown'])}",
            'email': f"contact@{name.lower().replace(' ', '')}.com",
            'phone': f"555-{random.randint(1000, 9999)}",
            'created_by': random.choice(users)
        }
    )
    if created:
        print(f"Created supplier: {name}")
        
        # Create products for this supplier
        for j in range(2):
            Product.objects.create(
                name=f"Product {j+1} from {name}",
                sku=f"SKU-{supplier.id}-{j+1}",
                description=f"Description for Product {j+1}",
                unit_price=Decimal(random.randint(10, 1000)),
                current_stock=random.randint(5, 50),
                min_stock_level=5,
                supplier=supplier
            )

print("Sample data creation completed!")
