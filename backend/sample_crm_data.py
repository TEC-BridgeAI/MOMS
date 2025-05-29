# backend/sample_crm_data.py
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
from apps.crm.models import Customer, Contact, Opportunity, Activity

# Clear existing CRM data
print("Clearing existing CRM data...")
Activity.objects.all().delete()
Opportunity.objects.all().delete()
Contact.objects.all().delete()
Customer.objects.all().delete()
print("Existing CRM data cleared.")

# Get users for assigning ownership
users = User.objects.all()
if not users:
    print("No users found. Please run the HR data script first.")
    exit()

# Create customers
customers = [
    {
        "name": "Acme Corporation", 
        "type": "company",
        "email": "info@acmecorp.com",
        "phone": "555-123-4567",
        "address": "123 Main St, Anytown, USA",
        "website": "https://www.acmecorp.com"
    },
    {
        "name": "TechNova Solutions", 
        "type": "company",
        "email": "contact@technovasolutions.com",
        "phone": "555-987-6543",
        "address": "456 Innovation Way, Tech City, USA",
        "website": "https://www.technovasolutions.com"
    },
    {
        "name": "Global Enterprises", 
        "type": "company",
        "email": "info@globalenterprises.com",
        "phone": "555-456-7890",
        "address": "789 Corporate Blvd, Metropolis, USA",
        "website": "https://www.globalenterprises.com"
    },
    {
        "name": "Sunshine Retail", 
        "type": "company",
        "email": "sales@sunshineretail.com",
        "phone": "555-789-0123",
        "address": "321 Commerce Ave, Market Town, USA",
        "website": "https://www.sunshineretail.com"
    },
    {
        "name": "John Smith", 
        "type": "individual",
        "email": "john.smith@example.com",
        "phone": "555-234-5678",
        "address": "567 Residential St, Hometown, USA",
        "website": None
    },
    {
        "name": "Sarah Johnson", 
        "type": "individual",
        "email": "sarah.johnson@example.com",
        "phone": "555-345-6789",
        "address": "890 Maple Ave, Springfield, USA",
        "website": None
    }
]

created_customers = []
for cust_data in customers:
    # Select a random user as owner
    assigned_to = random.choice(users)
    created_by = random.choice(users)
    
    customer = Customer.objects.create(
        name=cust_data["name"],
        customer_type=cust_data["type"],
        email=cust_data["email"],
        phone=cust_data["phone"],
        address=cust_data["address"],
        website=cust_data["website"],
        assigned_to=assigned_to,
        created_by=created_by
    )
    created_customers.append(customer)
    print(f"Created customer: {customer.name}")

# Create contacts for company customers
contact_positions = [
    "CEO", "CTO", "CFO", "COO", "Sales Director", 
    "Marketing Manager", "IT Manager", "Procurement Manager"
]

for customer in Customer.objects.filter(customer_type='company'):
    # Create 2-4 contacts per company
    num_contacts = random.randint(2, 4)
    
    # Create primary contact
    first_name = random.choice(["John", "Michael", "David", "Robert", "James", "Sarah", "Jennifer", "Emily", "Lisa", "Mary"])
    last_name = random.choice(["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Wilson"])
    position = random.choice(contact_positions)
    
    primary_contact = Contact.objects.create(
        customer=customer,
        first_name=first_name,
        last_name=last_name,
        position=position,
        email=f"{first_name.lower()}.{last_name.lower()}@{customer.email.split('@')[1]}",
        phone=f"555-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
        is_primary=True
    )
    print(f"Created primary contact: {primary_contact.first_name} {primary_contact.last_name} for {customer.name}")
    
    # Create additional contacts
    for i in range(num_contacts - 1):
        first_name = random.choice(["John", "Michael", "David", "Robert", "James", "Sarah", "Jennifer", "Emily", "Lisa", "Mary"])
        last_name = random.choice(["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Wilson"])
        position = random.choice(contact_positions)
        
        contact = Contact.objects.create(
            customer=customer,
            first_name=first_name,
            last_name=last_name,
            position=position,
            email=f"{first_name.lower()}.{last_name.lower()}@{customer.email.split('@')[1]}",
            phone=f"555-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
            is_primary=False
        )
        print(f"Created contact: {contact.first_name} {contact.last_name} for {customer.name}")

# Create opportunities
opportunity_names = [
    "Annual Contract Renewal", "New Product Implementation", "Service Expansion", 
    "Software Upgrade", "Consulting Project", "Hardware Purchase", 
    "Maintenance Agreement", "Training Program", "Custom Development"
]

for customer in created_customers:
    # Create 1-3 opportunities per customer
    num_opportunities = random.randint(1, 3)
    
    for i in range(num_opportunities):
        name = f"{random.choice(opportunity_names)} - {customer.name}"
        amount = Decimal(random.randint(5000, 100000))
        status = random.choice(['new', 'qualified', 'proposal', 'negotiation', 'closed_won', 'closed_lost'])
        expected_close_date = datetime.now().date() + timedelta(days=random.randint(10, 90))
        
        assigned_to = random.choice(users)
        created_by = random.choice(users)
        
        opportunity = Opportunity.objects.create(
            name=name,
            customer=customer,
            amount=amount,
            status=status,
            expected_close_date=expected_close_date,
            description=f"Opportunity for {name} with estimated value of ${amount}",
            assigned_to=assigned_to,
            created_by=created_by
        )
        print(f"Created opportunity: {opportunity.name} (${opportunity.amount})")

# Create activities
activity_subjects = [
    "Initial Contact", "Follow-up Call", "Proposal Presentation", "Contract Negotiation", 
    "Product Demo", "Status Update", "Quarterly Review", "Issue Resolution"
]

# Create activities for each customer and opportunity
for customer in created_customers:
    # Create 2-5 activities per customer
    num_activities = random.randint(2, 5)
    
    for i in range(num_activities):
        activity_type = random.choice(['call', 'meeting', 'email', 'task', 'note'])
        subject = f"{random.choice(activity_subjects)} with {customer.name}"
        
        # Maybe link to an opportunity
        opportunity = None
        if random.choice([True, False]) and Opportunity.objects.filter(customer=customer).exists():
            opportunity = random.choice(list(Opportunity.objects.filter(customer=customer)))
        
        # Set due date (past, present, or future)
        time_offset = random.randint(-30, 30)  # Days from now
        due_date = datetime.now() + timedelta(days=time_offset)
        
        # Set completed status (past activities are more likely to be completed)
        completed = time_offset < 0 and random.choice([True, True, False])  # 2/3 chance for past activities
        
        created_by = random.choice(users)
        
        activity = Activity.objects.create(
            customer=customer,
            opportunity=opportunity,
            activity_type=activity_type,
            subject=subject,
            description=f"Activity details for {subject}",
            due_date=due_date,
            completed=completed,
            created_by=created_by
        )
        print(f"Created activity: {activity.subject} ({activity.activity_type})")

print("CRM sample data creation completed!")
