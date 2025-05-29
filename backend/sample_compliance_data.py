# backend/sample_compliance_data.py
import os
import django
import random
from datetime import datetime, timedelta

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moms_project.settings')
django.setup()

# Import models
from django.contrib.auth.models import User
from apps.compliance.models import Policy, Regulation, ComplianceTask, Audit

# Clear existing compliance data
print("Clearing existing compliance data...")
ComplianceTask.objects.all().delete()
Audit.objects.all().delete()
Policy.objects.all().delete()
Regulation.objects.all().delete()
print("Existing compliance data cleared.")

# Get users for assigning ownership
users = User.objects.all()
if not users:
    print("No users found. Please run the HR data script first.")
    exit()

# Create regulations
regulations = [
    {
        "name": "GDPR", 
        "description": "General Data Protection Regulation - EU regulation on data protection and privacy",
        "authority": "European Union",
        "reference_url": "https://gdpr.eu/",
        "effective_date": datetime(2018, 5, 25).date()
    },
    {
        "name": "HIPAA", 
        "description": "Health Insurance Portability and Accountability Act - US legislation for data privacy in healthcare",
        "authority": "U.S. Department of Health & Human Services",
        "reference_url": "https://www.hhs.gov/hipaa/",
        "effective_date": datetime(1996, 8, 21).date()
    },
    {
        "name": "SOX", 
        "description": "Sarbanes-Oxley Act - US law for public company boards and accounting firms",
        "authority": "U.S. Securities and Exchange Commission",
        "reference_url": "https://www.sec.gov/",
        "effective_date": datetime(2002, 7, 30).date()
    },
    {
        "name": "PCI DSS", 
        "description": "Payment Card Industry Data Security Standard - Information security standard for credit card processing",
        "authority": "PCI Security Standards Council",
        "reference_url": "https://www.pcisecuritystandards.org/",
        "effective_date": datetime(2004, 12, 15).date()
    },
    {
        "name": "ISO 27001", 
        "description": "International standard for information security management",
        "authority": "International Organization for Standardization",
        "reference_url": "https://www.iso.org/isoiec-27001-information-security.html",
        "effective_date": datetime(2005, 10, 15).date()
    }
]

created_regulations = []
for reg_data in regulations:
    regulation = Regulation.objects.create(
        name=reg_data["name"],
        description=reg_data["description"],
        authority=reg_data["authority"],
        reference_url=reg_data["reference_url"],
        effective_date=reg_data["effective_date"]
    )
    created_regulations.append(regulation)
    print(f"Created regulation: {regulation.name}")

# Create policies
policies = [
    {
        "title": "Data Protection Policy", 
        "description": "Guidelines for handling personal and sensitive data",
        "content": "This policy outlines the procedures for collecting, storing, and processing personal data in compliance with relevant regulations.",
        "status": "active",
        "version": "1.2",
        "effective_date": datetime.now().date() - timedelta(days=90),
        "review_date": datetime.now().date() + timedelta(days=275)
    },
    {
        "title": "Information Security Policy", 
        "description": "Standards for maintaining information security",
        "content": "This policy defines the security controls and practices required to protect company and customer information assets.",
        "status": "active",
        "version": "2.1",
        "effective_date": datetime.now().date() - timedelta(days=120),
        "review_date": datetime.now().date() + timedelta(days=245)
    },
    {
        "title": "Code of Conduct", 
        "description": "Ethical guidelines for employee behavior",
        "content": "This code outlines the ethical standards and behaviors expected of all employees in their professional activities.",
        "status": "active",
        "version": "3.0",
        "effective_date": datetime.now().date() - timedelta(days=200),
        "review_date": datetime.now().date() + timedelta(days=165)
    },
    {
        "title": "Acceptable Use Policy", 
        "description": "Guidelines for appropriate use of company IT resources",
        "content": "This policy defines the acceptable use of company computing resources, networks, and data systems.",
        "status": "active",
        "version": "1.5",
        "effective_date": datetime.now().date() - timedelta(days=150),
        "review_date": datetime.now().date() + timedelta(days=215)
    },
    {
        "title": "Incident Response Plan", 
        "description": "Procedures for responding to security incidents",
        "content": "This plan outlines the steps to be taken in the event of a security breach or data incident.",
        "status": "draft",
        "version": "0.9",
        "effective_date": datetime.now().date() + timedelta(days=15),
        "review_date": datetime.now().date() + timedelta(days=380)
    }
]

created_policies = []
for policy_data in policies:
    created_by = random.choice(users)
    policy = Policy.objects.create(
        title=policy_data["title"],
        description=policy_data["description"],
        content=policy_data["content"],
        status=policy_data["status"],
        version=policy_data["version"],
        effective_date=policy_data["effective_date"],
        review_date=policy_data["review_date"],
        created_by=created_by
    )
    created_policies.append(policy)
    print(f"Created policy: {policy.title} (v{policy.version})")

# Create compliance tasks
task_templates = [
    {"title": "Annual {policy} Review", "description": "Conduct annual review of the {policy} to ensure it remains current and effective."},
    {"title": "{regulation} Compliance Assessment", "description": "Assess current practices against {regulation} requirements and identify gaps."},
    {"title": "Update {policy} for {regulation}", "description": "Update {policy} to address recent changes in {regulation} requirements."},
    {"title": "{policy} Training for Staff", "description": "Conduct training sessions to ensure staff understand and follow the {policy}."},
    {"title": "{regulation} Audit Preparation", "description": "Prepare documentation and evidence for upcoming {regulation} compliance audit."}
]

# Create 10-15 compliance tasks
num_tasks = random.randint(10, 15)
for i in range(num_tasks):
    # Select a random task template
    task_template = random.choice(task_templates)
    
    # Randomly select policy and/or regulation
    use_policy = random.choice([True, False, True])  # Bias toward using policies
    use_regulation = not use_policy or random.choice([True, False])
    
    policy = random.choice(created_policies) if use_policy and created_policies else None
    regulation = random.choice(created_regulations) if use_regulation and created_regulations else None
    
    # Format title and description
    policy_name = policy.title if policy else "Policy"
    regulation_name = regulation.name if regulation else "Regulation"
    
    title = task_template["title"].format(
        policy=policy_name,
        regulation=regulation_name
    )
    
    description = task_template["description"].format(
        policy=policy_name,
        regulation=regulation_name
    )
    
    # Assign to a random user
    assigned_to = random.choice(users)
    created_by = random.choice(users)
    
    # Set due date (between 1 and 90 days from now)
    due_date = datetime.now().date() + timedelta(days=random.randint(1, 90))
    
    # Set priority and status
    priority = random.choice(['low', 'medium', 'high', 'critical'])
    status = random.choice(['pending', 'in_progress', 'completed', 'overdue'])
    
    task = ComplianceTask.objects.create(
        title=title,
        description=description,
        policy=policy,
        regulation=regulation,
        assigned_to=assigned_to,
        due_date=due_date,
        status=status,
        priority=priority,
        created_by=created_by
    )
    print(f"Created compliance task: {task.title}")

# Create audits
audit_templates = [
    {"title": "Annual Security Audit", "description": "Comprehensive review of security controls and practices."},
    {"title": "{regulation} Compliance Audit", "description": "Formal audit of compliance with {regulation} requirements."},
    {"title": "Internal Policy Review", "description": "Internal audit of policy implementation and adherence."},
    {"title": "Vendor Compliance Assessment", "description": "Audit of key vendors' compliance with security and privacy requirements."},
    {"title": "Data Protection Impact Assessment", "description": "Assessment of data processing activities and associated risks."}
]

# Create 3-6 audits
num_audits = random.randint(3, 6)
for i in range(num_audits):
    # Select a random audit template
    audit_template = random.choice(audit_templates)
    
    # Maybe reference a regulation
    regulation_name = ""
    if "regulation" in audit_template["title"] and created_regulations:
        regulation = random.choice(created_regulations)
        regulation_name = regulation.name
    
    # Format title and description
    title = audit_template["title"].format(regulation=regulation_name)
    description = audit_template["description"].format(regulation=regulation_name)
    
    # Set dates
    start_date = datetime.now().date() - timedelta(days=random.randint(0, 30))
    end_date = start_date + timedelta(days=random.randint(5, 30))
    
    # Set status based on dates
    today = datetime.now().date()
    if end_date < today:
        status = 'completed'
        findings = "Audit completed. " + random.choice([
            "No major findings identified.",
            "Several minor issues identified and addressed.",
            "One major finding requiring immediate attention.",
            "Multiple compliance gaps identified, remediation plan in progress."
        ])
    elif start_date <= today:
        status = 'in_progress'
        findings = "Audit in progress. Preliminary findings being documented."
    else:
        status = 'planned'
        findings = None
    
    created_by = random.choice(users)
    
    audit = Audit.objects.create(
        title=title,
        description=description,
        start_date=start_date,
        end_date=end_date,
        status=status,
        findings=findings,
        created_by=created_by
    )
    print(f"Created audit: {audit.title} ({audit.status})")

print("Compliance sample data creation completed!")
