# backend/sample_supply_chain_data.py
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
from apps.supply_chain.models import Supplier, Product, PurchaseOrder, PurchaseOrderItem

# Clear existing supply chain data
print("Clearing existing supply chain data...")
PurchaseOrderItem.objects.all().delete()
PurchaseOrder.objects.all().delete()
Product.objects.all().delete()
Supplier.objects.all().delete()
print("Existing supply chain data cleared.")

# Get users for assigning ownership
users = User.objects.all()
if not users:
    print("No users found. Please run the HR data script first.")
    exit()

# Create suppliers
suppliers = [
    {
        "name": "TechComponents Inc.", 
        "contact_name": "Michael Johnson",
        "email": "mjohnson@techcomponents.com",
        "phone": "555-123-4567",
        "address": "123 Tech Blvd, Silicon Valley, CA",
        "website": "https://www.techcomponents.com",
        "notes": "Primary supplier for electronic components"
    },
    {
        "name": "Global Office Supplies", 
        "contact_name": "Sarah Williams",
        "email": "swilliams@globaloffice.com",
        "phone": "555-234-5678",
        "address": "456 Supply St, Chicago, IL",
        "website": "https://www.globalofficesupplies.com",
        "notes": "Office supplies and furniture"
    },
    {
        "name": "FastShip Logistics", 
        "contact_name": "David Brown",
        "email": "dbrown@fastship.com",
        "phone": "555-345-6789",
        "address": "789 Shipping Lane, Atlanta, GA",
        "website": "https://www.fastshiplogistics.com",
        "notes": "Shipping and logistics partner"
    },
    {
        "name": "Quality Manufacturing Co.", 
        "contact_name": "Jennifer Miller",
        "email": "jmiller@qualitymfg.com",
        "phone": "555-456-7890",
        "address": "101 Factory Rd, Detroit, MI",
        "website": "https://www.qualitymfg.com",
        "notes": "Custom manufacturing partner"
    },
    {
        "name": "EcoPackaging Solutions", 
        "contact_name": "Robert Davis",
        "email": "rdavis@ecopackaging.com",
        "phone": "555-567-8901",
        "address": "202 Green Way, Portland, OR",
        "website": "https://www.ecopackaging.com",
        "notes": "Sustainable packaging materials"
    }
]

created_suppliers = []
for supplier_data in suppliers:
    created_by = random.choice(users)
    
    supplier = Supplier.objects.create(
        name=supplier_data["name"],
        contact_name=supplier_data["contact_name"],
        email=supplier_data["email"],
        phone=supplier_data["phone"],
        address=supplier_data["address"],
        website=supplier_data["website"],
        notes=supplier_data["notes"],
        created_by=created_by
    )
    created_suppliers.append(supplier)
    print(f"Created supplier: {supplier.name}")

# Create products
product_categories = {
    "TechComponents Inc.": [
        {"name": "CPU Processor", "sku": "CPU-001", "unit": "each", "price_range": (200, 800)},
        {"name": "RAM Module 16GB", "sku": "RAM-16GB", "unit": "each", "price_range": (50, 150)},
        {"name": "SSD Drive 1TB", "sku": "SSD-1TB", "unit": "each", "price_range": (100, 300)},
        {"name": "Graphics Card", "sku": "GPU-001", "unit": "each", "price_range": (300, 1200)},
        {"name": "Motherboard", "sku": "MB-001", "unit": "each", "price_range": (150, 400)}
    ],
    "Global Office Supplies": [
        {"name": "Office Paper", "sku": "PAP-A4", "unit": "ream", "price_range": (3, 8)},
        {"name": "Ballpoint Pens", "sku": "PEN-001", "unit": "box", "price_range": (5, 15)},
        {"name": "Office Chair", "sku": "CHAIR-001", "unit": "each", "price_range": (100, 300)},
        {"name": "Desk Lamp", "sku": "LAMP-001", "unit": "each", "price_range": (20, 60)},
        {"name": "Filing Cabinet", "sku": "CAB-001", "unit": "each", "price_range": (80, 200)}
    ],
    "FastShip Logistics": [
        {"name": "Shipping Labels", "sku": "LAB-001", "unit": "roll", "price_range": (10, 30)},
        {"name": "Packaging Tape", "sku": "TAPE-001", "unit": "roll", "price_range": (3, 8)},
        {"name": "Shipping Boxes - Small", "sku": "BOX-S", "unit": "bundle", "price_range": (15, 40)},
        {"name": "Shipping Boxes - Medium", "sku": "BOX-M", "unit": "bundle", "price_range": (20, 50)},
        {"name": "Shipping Boxes - Large", "sku": "BOX-L", "unit": "bundle", "price_range": (25, 60)}
    ],
    "Quality Manufacturing Co.": [
        {"name": "Metal Brackets", "sku": "BRKT-001", "unit": "box", "price_range": (30, 80)},
        {"name": "Custom Enclosure", "sku": "ENC-001", "unit": "each", "price_range": (50, 150)},
        {"name": "Mounting Hardware", "sku": "MNT-001", "unit": "kit", "price_range": (15, 40)},
        {"name": "Plastic Components", "sku": "PLST-001", "unit": "box", "price_range": (20, 60)},
        {"name": "Assembly Service", "sku": "SVC-ASM", "unit": "hour", "price_range": (40, 100)}
    ],
    "EcoPackaging Solutions": [
        {"name": "Recycled Cardboard Boxes", "sku": "ECO-BOX", "unit": "bundle", "price_range": (20, 50)},
        {"name": "Biodegradable Packing Peanuts", "sku": "ECO-PNUT", "unit": "bag", "price_range": (15, 35)},
        {"name": "Paper Packaging Tape", "sku": "ECO-TAPE", "unit": "roll", "price_range": (4, 10)},
        {"name": "Compostable Mailers", "sku": "ECO-MAIL", "unit": "pack", "price_range": (10, 30)},
        {"name": "Recycled Tissue Paper", "sku": "ECO-TISS", "unit": "ream", "price_range": (5, 15)}
    ]
}

created_products = []
for supplier in created_suppliers:
    # Get product templates for this supplier
    product_templates = product_categories.get(supplier.name, [])
    
    if not product_templates:
        # Use generic products if no specific ones defined
        product_templates = [
            {"name": f"Product {i+1}", "sku": f"PROD-{i+1:03d}", "unit": "each", "price_range": (10, 100)}
            for i in range(5)
        ]
    
    for product_data in product_templates:
        # Set random price within range
        unit_price = Decimal(random.uniform(product_data["price_range"][0], product_data["price_range"][1])).quantize(Decimal('0.01'))
        
        # Set random stock levels
        min_stock = random.randint(5, 20)
        current_stock = random.randint(0, 50)
        
        product = Product.objects.create(
            name=product_data["name"],
            sku=product_data["sku"],
            description=f"Description for {product_data['name']}",
            unit_price=unit_price,
            unit=product_data["unit"],
            min_stock_level=min_stock,
            current_stock=current_stock,
            supplier=supplier
        )
        created_products.append(product)
        print(f"Created product: {product.name} (${product.unit_price}/{product.unit})")

# Create purchase orders
# Create 10-15 purchase orders
num_purchase_orders = random.randint(10, 15)
for i in range(num_purchase_orders):
    # Select a random supplier
    supplier = random.choice(created_suppliers)
    
    # Set dates
    order_date = datetime.now().date() - timedelta(days=random.randint(0, 90))
    expected_delivery_date = order_date + timedelta(days=random.randint(3, 30))
    
    # Set status and delivery date based on order date
    today = datetime.now().date()
    if order_date > today - timedelta(days=3):
        status = random.choice(['draft', 'submitted'])
        delivery_date = None
    elif expected_delivery_date < today:
        status = 'received'
        delivery_date = expected_delivery_date
    elif order_date < today - timedelta(days=3):
        status = random.choice(['approved', 'shipped'])
        delivery_date = None
    else:
        status = 'submitted'
        delivery_date = None
    
    # Create purchase order
    order_number = f"PO-{order_date.strftime('%Y%m%d')}-{i+1:03d}"
    created_by = random.choice(users)
    
    purchase_order = PurchaseOrder.objects.create(
        order_number=order_number,
        supplier=supplier,
        status=status,
        order_date=order_date,
        expected_delivery_date=expected_delivery_date,
        delivery_date=delivery_date,
        notes=f"Purchase order for {supplier.name}",
        created_by=created_by
    )
    
    # Get products from this supplier
    supplier_products = Product.objects.filter(supplier=supplier)
    
    if supplier_products:
        # Create 1-5 items per purchase order
        num_items = random.randint(1, 5)
        selected_products = random.sample(list(supplier_products), min(num_items, len(supplier_products)))
        
        for product in selected_products:
            quantity = random.randint(1, 20)
            
            # Use product's unit price with small variation
            unit_price = product.unit_price * Decimal(random.uniform(0.95, 1.05)).quantize(Decimal('0.01'))
            
            PurchaseOrderItem.objects.create(
                purchase_order=purchase_order,
                product=product,
                quantity=quantity,
                unit_price=unit_price
            )
            print(f"Added item to PO {purchase_order.order_number}: {quantity} x {product.name}")
    
    print(f"Created purchase order: {purchase_order.order_number} ({status})")

print("Supply chain sample data creation completed!")
