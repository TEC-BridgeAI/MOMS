# backend/sample_finance_data.py
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
from apps.finance.models import Account, Transaction, TransactionLine, Invoice, InvoiceItem
from apps.crm.models import Customer

# Clear existing finance data
print("Clearing existing finance data...")
InvoiceItem.objects.all().delete()
Invoice.objects.all().delete()
TransactionLine.objects.all().delete()
Transaction.objects.all().delete()
Account.objects.all().delete()
print("Existing finance data cleared.")

# Get users for assigning ownership
users = User.objects.all()
if not users:
    print("No users found. Please run the HR data script first.")
    exit()

# Get customers for invoices
customers = Customer.objects.all()
if not customers:
    print("No customers found. Please run the CRM data script first.")
    exit()

# Create chart of accounts
accounts = [
    # Asset accounts
    {"name": "Cash", "code": "1000", "account_type": "asset", "description": "Cash on hand and in bank accounts"},
    {"name": "Accounts Receivable", "code": "1100", "account_type": "asset", "description": "Amounts owed by customers"},
    {"name": "Inventory", "code": "1200", "account_type": "asset", "description": "Goods held for sale"},
    {"name": "Office Equipment", "code": "1300", "account_type": "asset", "description": "Office furniture and equipment"},
    {"name": "Computer Equipment", "code": "1400", "account_type": "asset", "description": "Computers and related hardware"},
    
    # Liability accounts
    {"name": "Accounts Payable", "code": "2000", "account_type": "liability", "description": "Amounts owed to suppliers"},
    {"name": "Accrued Expenses", "code": "2100", "account_type": "liability", "description": "Expenses incurred but not yet paid"},
    {"name": "Loans Payable", "code": "2200", "account_type": "liability", "description": "Outstanding loans"},
    {"name": "Taxes Payable", "code": "2300", "account_type": "liability", "description": "Taxes owed but not yet paid"},
    
    # Equity accounts
    {"name": "Common Stock", "code": "3000", "account_type": "equity", "description": "Shareholders' equity"},
    {"name": "Retained Earnings", "code": "3100", "account_type": "equity", "description": "Accumulated profits"},
    
    # Revenue accounts
    {"name": "Sales Revenue", "code": "4000", "account_type": "revenue", "description": "Income from sales"},
    {"name": "Service Revenue", "code": "4100", "account_type": "revenue", "description": "Income from services"},
    {"name": "Interest Income", "code": "4200", "account_type": "revenue", "description": "Income from interest"},
    
    # Expense accounts
    {"name": "Salaries Expense", "code": "5000", "account_type": "expense", "description": "Employee salaries"},
    {"name": "Rent Expense", "code": "5100", "account_type": "expense", "description": "Office rent"},
    {"name": "Utilities Expense", "code": "5200", "account_type": "expense", "description": "Electricity, water, etc."},
    {"name": "Office Supplies Expense", "code": "5300", "account_type": "expense", "description": "Office supplies"},
    {"name": "Marketing Expense", "code": "5400", "account_type": "expense", "description": "Marketing and advertising"},
    {"name": "Travel Expense", "code": "5500", "account_type": "expense", "description": "Business travel"}
]

created_accounts = {}
for account_data in accounts:
    account = Account.objects.create(
        name=account_data["name"],
        code=account_data["code"],
        account_type=account_data["account_type"],
        description=account_data["description"]
    )
    created_accounts[account.code] = account
    print(f"Created account: {account.code} - {account.name}")

# Create transactions
transaction_templates = [
    {
        "description": "Monthly Payroll",
        "lines": [
            {"account_code": "5000", "description": "Salaries", "debit": lambda: Decimal(random.randint(5000, 15000))},
            {"account_code": "1000", "description": "Cash Payment", "credit": lambda: None}  # Will be balanced
        ]
    },
    {
        "description": "Office Rent Payment",
        "lines": [
            {"account_code": "5100", "description": "Monthly Rent", "debit": lambda: Decimal(random.randint(2000, 5000))},
            {"account_code": "1000", "description": "Cash Payment", "credit": lambda: None}  # Will be balanced
        ]
    },
    {
        "description": "Customer Payment",
        "lines": [
            {"account_code": "1000", "description": "Cash Receipt", "debit": lambda: Decimal(random.randint(1000, 10000))},
            {"account_code": "1100", "description": "Accounts Receivable", "credit": lambda: None}  # Will be balanced
        ]
    },
    {
        "description": "Sales Revenue",
        "lines": [
            {"account_code": "1100", "description": "Accounts Receivable", "debit": lambda: Decimal(random.randint(2000, 20000))},
            {"account_code": "4000", "description": "Product Sales", "credit": lambda: None}  # Will be balanced
        ]
    },
    {
        "description": "Purchase Office Supplies",
        "lines": [
            {"account_code": "5300", "description": "Office Supplies", "debit": lambda: Decimal(random.randint(100, 1000))},
            {"account_code": "1000", "description": "Cash Payment", "credit": lambda: None}  # Will be balanced
        ]
    }
]

# Create 15-20 transactions
num_transactions = random.randint(15, 20)
for i in range(num_transactions):
    # Select a random transaction template
    template = random.choice(transaction_templates)
    
    # Create transaction
    transaction_date = datetime.now().date() - timedelta(days=random.randint(0, 90))
    reference = f"TX-{transaction_date.strftime('%Y%m%d')}-{i+1:03d}"
    status = random.choice(['draft', 'posted', 'posted', 'posted'])  # Bias toward posted
    created_by = random.choice(users)
    
    transaction = Transaction.objects.create(
        date=transaction_date,
        reference=reference,
        description=template["description"],
        status=status,
        created_by=created_by
    )
    
    # Create transaction lines
    total_debit = Decimal('0.00')
    lines_to_create = []
    
    # First pass: create lines with specified amounts
    for line_data in template["lines"]:
        if line_data.get("debit") is not None:
            debit_amount = line_data["debit"]()
            total_debit += debit_amount
            lines_to_create.append({
                "account": created_accounts[line_data["account_code"]],
                "description": line_data["description"],
                "debit": debit_amount,
                "credit": Decimal('0.00')
            })
        elif line_data.get("credit") is not None and line_data["credit"]() is not None:
            credit_amount = line_data["credit"]()
            lines_to_create.append({
                "account": created_accounts[line_data["account_code"]],
                "description": line_data["description"],
                "debit": Decimal('0.00'),
                "credit": credit_amount
            })
    
    # Second pass: balance the transaction
    for line_data in template["lines"]:
        if (line_data.get("debit") is None and line_data.get("credit") is None) or \
           (line_data.get("credit") is not None and line_data["credit"]() is None):
            lines_to_create.append({
                "account": created_accounts[line_data["account_code"]],
                "description": line_data["description"],
                "debit": Decimal('0.00'),
                "credit": total_debit
            })
    
    # Create the lines
    for line_data in lines_to_create:
        TransactionLine.objects.create(
            transaction=transaction,
            account=line_data["account"],
            description=line_data["description"],
            debit=line_data["debit"],
            credit=line_data["credit"]
        )
    
    print(f"Created transaction: {transaction.reference} - {transaction.description}")

# Create invoices
# Create 10-15 invoices
num_invoices = random.randint(10, 15)
for i in range(num_invoices):
    # Select a random customer
    customer = random.choice(customers)
    
    # Create invoice
    invoice_date = datetime.now().date() - timedelta(days=random.randint(0, 60))
    due_date = invoice_date + timedelta(days=30)
    invoice_number = f"INV-{invoice_date.strftime('%Y%m%d')}-{i+1:03d}"
    
    # Determine status based on dates
    today = datetime.now().date()
    if invoice_date > today - timedelta(days=7):
        status = 'draft'
    elif due_date < today and random.choice([True, False]):
        status = 'overdue'
    elif random.choice([True, False, False]):  # 1/3 chance of being paid
        status = 'paid'
    else:
        status = 'sent'
    
    created_by = random.choice(users)
    
    # Maybe link to a transaction for paid invoices
    transaction = None
    if status == 'paid' and Transaction.objects.filter(status='posted').exists():
        transaction = random.choice(Transaction.objects.filter(status='posted'))
    
    invoice = Invoice.objects.create(
        customer=customer,
        invoice_number=invoice_number,
        date=invoice_date,
        due_date=due_date,
        status=status,
        notes=f"Invoice for {customer.name}",
        transaction=transaction,
        created_by=created_by
    )
    
    # Create 1-5 invoice items
    num_items = random.randint(1, 5)
    for j in range(num_items):
        description = random.choice([
            "Professional Services", "Consulting Hours", "Software License",
            "Hardware Purchase", "Maintenance Fee", "Support Hours",
            "Training Session", "Implementation Services", "Custom Development"
        ])
        
        quantity = Decimal(random.randint(1, 10))
        unit_price = Decimal(random.randint(100, 1000))
        
        InvoiceItem.objects.create(
            invoice=invoice,
            description=f"{description} - Item {j+1}",
            quantity=quantity,
            unit_price=unit_price
        )
    
    print(f"Created invoice: {invoice.invoice_number} for {customer.name} ({status})")

print("Finance sample data creation completed!")
