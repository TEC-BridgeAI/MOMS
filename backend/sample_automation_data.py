# backend/sample_analytics_data.py
import os
import django
import random
from datetime import datetime, timedelta
import json

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moms_project.settings')
django.setup()

# Import models
from django.contrib.auth.models import User
from apps.analytics.models import Dashboard, Report

# Clear existing analytics data
print("Clearing existing analytics data...")
Report.objects.all().delete()
Dashboard.objects.all().delete()
print("Existing analytics data cleared.")

# Get users for assigning ownership
users = User.objects.all()
if not users:
    print("No users found. Please run the HR data script first.")
    exit()

# Create dashboards
dashboards = [
    {"name": "Sales Overview", "description": "Key sales metrics and performance indicators"},
    {"name": "Marketing Analytics", "description": "Campaign performance and marketing ROI"},
    {"name": "Financial Performance", "description": "Revenue, expenses, and profitability metrics"},
    {"name": "HR Dashboard", "description": "Employee metrics and HR KPIs"},
    {"name": "Operations Metrics", "description": "Operational efficiency and performance"}
]

created_dashboards = []
for dash_data in dashboards:
    created_by = random.choice(users)
    dashboard = Dashboard.objects.create(
        name=dash_data["name"],
        description=dash_data["description"],
        created_by=created_by
    )
    created_dashboards.append(dashboard)
    print(f"Created dashboard: {dashboard.name}")

# Create reports with sample configurations
report_types = ['bar', 'line', 'pie', 'table', 'kpi']

for dashboard in created_dashboards:
    # Create 3-5 reports per dashboard
    num_reports = random.randint(3, 5)
    for i in range(num_reports):
        report_type = random.choice(report_types)
        
        # Create appropriate config based on report type
        if report_type == 'bar':
            config = {
                'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                'datasets': [
                    {
                        'label': 'Dataset 1',
                        'data': [random.randint(10, 100) for _ in range(6)]
                    },
                    {
                        'label': 'Dataset 2',
                        'data': [random.randint(10, 100) for _ in range(6)]
                    }
                ],
                'options': {
                    'title': f'Sample {report_type.capitalize()} Chart',
                    'xAxisLabel': 'Month',
                    'yAxisLabel': 'Value'
                }
            }
        elif report_type == 'line':
            config = {
                'labels': ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5'],
                'datasets': [
                    {
                        'label': 'Trend',
                        'data': [random.randint(20, 80) for _ in range(5)]
                    }
                ],
                'options': {
                    'title': f'Sample {report_type.capitalize()} Chart',
                    'xAxisLabel': 'Week',
                    'yAxisLabel': 'Value'
                }
            }
        elif report_type == 'pie':
            config = {
                'labels': ['Category A', 'Category B', 'Category C', 'Category D'],
                'datasets': [
                    {
                        'data': [random.randint(10, 30) for _ in range(4)]
                    }
                ],
                'options': {
                    'title': f'Sample {report_type.capitalize()} Chart'
                }
            }
        elif report_type == 'table':
            config = {
                'headers': ['Name', 'Value', 'Change'],
                'rows': [
                    ['Item 1', random.randint(100, 500), f"{random.randint(-10, 20)}%"],
                    ['Item 2', random.randint(100, 500), f"{random.randint(-10, 20)}%"],
                    ['Item 3', random.randint(100, 500), f"{random.randint(-10, 20)}%"],
                    ['Item 4', random.randint(100, 500), f"{random.randint(-10, 20)}%"]
                ]
            }
        else:  # kpi
            config = {
                'value': random.randint(50, 150),
                'target': 100,
                'unit': '%',
                'trend': random.choice(['up', 'down', 'stable'])
            }
        
        # Sample SQL queries based on report context
        queries = {
            'Sales Overview': "SELECT date, SUM(amount) FROM sales GROUP BY date",
            'Marketing Analytics': "SELECT campaign, COUNT(leads) FROM marketing_campaigns GROUP BY campaign",
            'Financial Performance': "SELECT month, revenue, expenses FROM financial_data",
            'HR Dashboard': "SELECT department, COUNT(employees) FROM employees GROUP BY department",
            'Operations Metrics': "SELECT process, avg_completion_time FROM operations_data"
        }
        
        report = Report.objects.create(
            title=f"{dashboard.name} - Report {i+1}",
            description=f"Sample report for {dashboard.name}",
            dashboard=dashboard,
            report_type=report_type,
            query=queries.get(dashboard.name, "SELECT * FROM sample_data"),
            config=config,
            created_by=random.choice(users)
        )
        print(f"Created report: {report.title} ({report_type})")

print("Analytics sample data creation completed!")
