# backend/sample_strategy_data.py
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
from apps.strategy.models import StrategicPlan, Goal, Objective, KeyResult

# Clear existing strategy data
print("Clearing existing strategy data...")
KeyResult.objects.all().delete()
Objective.objects.all().delete()
Goal.objects.all().delete()
StrategicPlan.objects.all().delete()
print("Existing strategy data cleared.")

# Get users for assigning ownership
users = User.objects.all()
if not users:
    print("No users found. Please run the HR data script first.")
    exit()

# Create strategic plans
strategic_plans = [
    {
        "title": "Five-Year Growth Strategy", 
        "description": "Long-term strategic plan for sustainable company growth",
        "status": "active",
        "start_date": datetime.now().date() - timedelta(days=30),
        "end_date": datetime.now().date() + timedelta(days=365*5)
    },
    {
        "title": "Digital Transformation Initiative", 
        "description": "Strategic plan for digital transformation across all business units",
        "status": "active",
        "start_date": datetime.now().date() - timedelta(days=60),
        "end_date": datetime.now().date() + timedelta(days=365*2)
    },
    {
        "title": "Market Expansion Plan", 
        "description": "Strategy for expanding into new markets and territories",
        "status": "draft",
        "start_date": datetime.now().date() + timedelta(days=30),
        "end_date": datetime.now().date() + timedelta(days=365*3)
    }
]

created_plans = []
for plan_data in strategic_plans:
    created_by = random.choice(users)
    
    plan = StrategicPlan.objects.create(
        title=plan_data["title"],
        description=plan_data["description"],
        status=plan_data["status"],
        start_date=plan_data["start_date"],
        end_date=plan_data["end_date"],
        created_by=created_by
    )
    created_plans.append(plan)
    print(f"Created strategic plan: {plan.title}")

# Create goals for each strategic plan
goal_templates = [
    # Growth goals
    {"title": "Increase Revenue", "description": "Increase annual revenue through new sales and existing customer growth", "priority": "high"},
    {"title": "Expand Customer Base", "description": "Acquire new customers in target markets", "priority": "high"},
    {"title": "Improve Profit Margins", "description": "Enhance profitability through cost optimization and pricing strategy", "priority": "high"},
    {"title": "Enter New Markets", "description": "Expand into new geographic or product markets", "priority": "medium"},
    
    # Operational goals
    {"title": "Enhance Operational Efficiency", "description": "Improve internal processes and reduce operational costs", "priority": "medium"},
    {"title": "Optimize Supply Chain", "description": "Improve supply chain efficiency and reduce costs", "priority": "medium"},
    {"title": "Reduce Environmental Impact", "description": "Implement sustainable practices and reduce carbon footprint", "priority": "low"},
    
    # People goals
    {"title": "Improve Employee Satisfaction", "description": "Enhance workplace culture and employee engagement", "priority": "medium"},
    {"title": "Develop Leadership Pipeline", "description": "Identify and develop future leaders within the organization", "priority": "medium"},
    {"title": "Enhance Talent Acquisition", "description": "Improve recruitment processes to attract top talent", "priority": "low"},
    
    # Innovation goals
    {"title": "Increase R&D Investment", "description": "Allocate more resources to research and development", "priority": "medium"},
    {"title": "Launch New Products", "description": "Develop and launch innovative new products", "priority": "high"},
    {"title": "Implement New Technologies", "description": "Adopt emerging technologies to improve operations", "priority": "medium"}
]

for plan in created_plans:
    # Create 4-6 goals per strategic plan
    num_goals = random.randint(4, 6)
    selected_goals = random.sample(goal_templates, num_goals)
    
    for goal_data in selected_goals:
        # Set status based on plan status and random chance
        if plan.status == "draft":
            status = "not_started"
        else:
            status = random.choice(["not_started", "in_progress", "in_progress", "completed"])
        
        # Set target date within plan timeframe
        days_range = (plan.end_date - plan.start_date).days
        target_offset = random.randint(int(days_range * 0.3), int(days_range * 0.8))
        target_date = plan.start_date + timedelta(days=target_offset)
        
        # Assign to a random user
        responsible = random.choice(users)
        
        goal = Goal.objects.create(
            strategic_plan=plan,
            title=goal_data["title"],
            description=goal_data["description"],
            priority=goal_data["priority"],
            status=status,
            target_date=target_date,
            responsible=responsible
        )
        print(f"Created goal: {goal.title} for {plan.title}")
        
        # Create 2-4 objectives per goal
        num_objectives = random.randint(2, 4)
        
        for i in range(num_objectives):
            # Set objective status based on goal status
            if goal.status == "completed":
                obj_status = "completed"
            elif goal.status == "in_progress":
                obj_status = random.choice(["not_started", "in_progress", "completed"])
            else:
                obj_status = "not_started"
            
            # Set target date before goal target date
            obj_target_date = goal.target_date - timedelta(days=random.randint(30, 90))
            
            objective = Objective.objects.create(
                goal=goal,
                title=f"Objective {i+1} for {goal.title}",
                description=f"Specific objective to achieve {goal.title}",
                status=obj_status,
                target_date=obj_target_date
            )
            print(f"Created objective: {objective.title}")
            
            # Create 1-3 key results per objective
            num_key_results = random.randint(1, 3)
            
            for j in range(num_key_results):
                # Set target value and current value based on objective status
                target_value = Decimal(random.randint(50, 1000))
                
                if objective.status == "completed":
                    current_value = target_value
                elif objective.status == "in_progress":
                    current_value = target_value * Decimal(random.uniform(0.3, 0.8))
                else:
                    current_value = Decimal('0.00')
                
                # Set unit based on key result type
                unit_type = random.choice(["count", "percentage", "currency", "score"])
                if unit_type == "count":
                    unit = "items"
                elif unit_type == "percentage":
                    unit = "%"
                elif unit_type == "currency":
                    unit = "$"
                else:
                    unit = "points"
                
                key_result = KeyResult.objects.create(
                    objective=objective,
                    title=f"KR {j+1}: {random.choice(['Achieve', 'Reach', 'Attain', 'Complete'])} {target_value} {unit}",
                    description=f"Key result to measure progress on {objective.title}",
                    target_value=target_value,
                    current_value=current_value,
                    unit=unit
                )
                print(f"Created key result: {key_result.title} ({key_result.current_value}/{key_result.target_value} {key_result.unit})")

print("Strategy sample data creation completed!")
