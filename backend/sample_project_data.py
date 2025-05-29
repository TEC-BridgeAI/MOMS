# backend/sample_project_data.py
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
from apps.project.models import Project, Task, TimeEntry, Milestone

# Clear existing project data
print("Clearing existing project data...")
TimeEntry.objects.all().delete()
Task.objects.all().delete()
Milestone.objects.all().delete()
Project.objects.all().delete()
print("Existing project data cleared.")

# Get users for assigning ownership
users = User.objects.all()
if not users:
    print("No users found. Please run the HR data script first.")
    exit()

# Create projects
projects = [
    {
        "name": "Website Redesign", 
        "description": "Redesign and relaunch of the company website with improved UX/UI",
        "status": "active",
        "budget": Decimal("50000.00")
    },
    {
        "name": "Mobile App Development", 
        "description": "Development of a new mobile application for iOS and Android",
        "status": "active",
        "budget": Decimal("75000.00")
    },
    {
        "name": "CRM Implementation", 
        "description": "Implementation of a new customer relationship management system",
        "status": "planning",
        "budget": Decimal("35000.00")
    },
    {
        "name": "Office Relocation", 
        "description": "Planning and execution of office move to new location",
        "status": "on_hold",
        "budget": Decimal("25000.00")
    },
    {
        "name": "Annual Marketing Campaign", 
        "description": "Planning and execution of annual marketing campaign",
        "status": "active",
        "budget": Decimal("45000.00")
    },
    {
        "name": "Product Launch", 
        "description": "Launch of new product line including marketing and distribution",
        "status": "completed",
        "budget": Decimal("60000.00")
    }
]

created_projects = []
for proj_data in projects:
    # Set dates based on status
    today = datetime.now().date()
    
    if proj_data["status"] == "completed":
        start_date = today - timedelta(days=random.randint(180, 365))
        end_date = today - timedelta(days=random.randint(10, 60))
    elif proj_data["status"] == "planning":
        start_date = today + timedelta(days=random.randint(10, 30))
        end_date = start_date + timedelta(days=random.randint(90, 180))
    else:  # active or on_hold
        start_date = today - timedelta(days=random.randint(30, 90))
        end_date = today + timedelta(days=random.randint(30, 180))
    
    # Select a random user as manager
    manager = random.choice(users)
    created_by = random.choice(users)
    
    project = Project.objects.create(
        name=proj_data["name"],
        description=proj_data["description"],
        status=proj_data["status"],
        start_date=start_date,
        end_date=end_date,
        budget=proj_data["budget"],
        manager=manager,
        created_by=created_by
    )
    
    # Add 3-6 random members to the project
    team_size = random.randint(3, 6)
    team_members = random.sample(list(users), min(team_size, len(users)))
    project.members.add(*team_members)
    
    created_projects.append(project)
    print(f"Created project: {project.name} ({project.status})")

# Create milestones for each project
milestone_templates = [
    {"title": "Project Kickoff", "relative_days": 0},
    {"title": "Requirements Gathering", "relative_days": 14},
    {"title": "Design Phase Complete", "relative_days": 30},
    {"title": "Development Complete", "relative_days": 60},
    {"title": "Testing Complete", "relative_days": 75},
    {"title": "User Acceptance Testing", "relative_days": 85},
    {"title": "Project Launch", "relative_days": 90}
]

for project in created_projects:
    # Create 3-5 milestones per project
    num_milestones = random.randint(3, 5)
    selected_milestones = random.sample(milestone_templates, num_milestones)
    
    # Sort by relative days
    selected_milestones.sort(key=lambda x: x["relative_days"])
    
    for milestone_data in selected_milestones:
        due_date = project.start_date + timedelta(days=milestone_data["relative_days"])
        completed = project.status == "completed" or (due_date < datetime.now().date() and random.choice([True, False]))
        
        milestone = Milestone.objects.create(
            project=project,
            title=milestone_data["title"],
            description=f"Milestone for {project.name}: {milestone_data['title']}",
            due_date=due_date,
            completed=completed
        )
        print(f"Created milestone: {milestone.title} for {project.name}")

# Create tasks for each project
task_templates = [
    # Design tasks
    {"title": "Create wireframes", "description": "Design wireframes for all pages", "priority": "medium", "estimated_hours": 20},
    {"title": "Design mockups", "description": "Create visual mockups based on wireframes", "priority": "medium", "estimated_hours": 30},
    {"title": "Design review", "description": "Review and finalize designs", "priority": "high", "estimated_hours": 8},
    
    # Development tasks
    {"title": "Set up development environment", "description": "Configure development environment and tools", "priority": "high", "estimated_hours": 8},
    {"title": "Implement frontend", "description": "Develop frontend components and pages", "priority": "high", "estimated_hours": 40},
    {"title": "Implement backend", "description": "Develop backend services and APIs", "priority": "high", "estimated_hours": 40},
    {"title": "Database setup", "description": "Set up and configure database", "priority": "medium", "estimated_hours": 16},
    
    # Testing tasks
    {"title": "Write unit tests", "description": "Create automated unit tests", "priority": "medium", "estimated_hours": 24},
    {"title": "Perform integration testing", "description": "Test integration between components", "priority": "high", "estimated_hours": 16},
    {"title": "User acceptance testing", "description": "Conduct UAT with stakeholders", "priority": "high", "estimated_hours": 24},
    
    # Documentation tasks
    {"title": "Create user documentation", "description": "Write user guides and documentation", "priority": "low", "estimated_hours": 16},
    {"title": "Technical documentation", "description": "Document technical aspects and architecture", "priority": "low", "estimated_hours": 16},
    
    # Project management tasks
    {"title": "Weekly status meeting", "description": "Regular team status meeting", "priority": "medium", "estimated_hours": 2},
    {"title": "Project planning", "description": "Plan project phases and resources", "priority": "high", "estimated_hours": 8},
    {"title": "Stakeholder reporting", "description": "Prepare and deliver stakeholder reports", "priority": "medium", "estimated_hours": 4}
]

for project in created_projects:
    # Create 8-12 tasks per project
    num_tasks = random.randint(8, 12)
    selected_tasks = random.sample(task_templates, min(num_tasks, len(task_templates)))
    
    # Track created tasks for parent-child relationships
    project_tasks = []
    
    for i, task_data in enumerate(selected_tasks):
        # Set status based on project status and random chance
        if project.status == "completed":
            status = "done"
        elif project.status == "planning":
            status = "todo"
        else:
            status = random.choice(["todo", "in_progress", "review", "done"])
        
        # Set due date
        if status == "done":
            due_date = datetime.now().date() - timedelta(days=random.randint(1, 30))
        else:
            due_date = datetime.now().date() + timedelta(days=random.randint(1, 60))
        
        # Assign to a project member
        if project.members.exists():
            assigned_to = random.choice(list(project.members.all()))
        else:
            assigned_to = project.manager
        
        # Maybe set a parent task (20% chance if not the first task)
        parent_task = None
        if i > 0 and project_tasks and random.random() < 0.2:
            parent_task = random.choice(project_tasks)
        
        task = Task.objects.create(
            project=project,
            title=task_data["title"],
            description=task_data["description"],
            priority=task_data["priority"],
            status=status,
            assigned_to=assigned_to,
            due_date=due_date,
            estimated_hours=task_data["estimated_hours"],
            parent_task=parent_task,
            created_by=project.created_by
        )
        
        project_tasks.append(task)
        print(f"Created task: {task.title} for {project.name} ({status})")
        
        # Create time entries for completed or in-progress tasks
        if status in ["done", "in_progress"]:
            # Create 1-5 time entries
            num_entries = random.randint(1, 5)
            total_hours = 0
            
            for j in range(num_entries):
                # Time entries should be in the past
                entry_date = datetime.now().date() - timedelta(days=random.randint(1, 30))
                
                # Hours should sum up to roughly the estimated hours for completed tasks
                if status == "done" and j == num_entries - 1:
                    # Last entry for completed task - make hours add up to roughly estimated
                    hours = max(1, task.estimated_hours - total_hours + random.randint(-2, 2))
                else:
                    max_hours = max(1, task.estimated_hours // 2)
                    hours = Decimal(random.randint(1, max_hours))
                
                total_hours += hours
                
                # User who logged time should be the assignee or another team member
                if random.random() < 0.8:  # 80% chance it's the assignee
                    user = assigned_to
                elif project.members.exists():
                    user = random.choice(list(project.members.all()))
                else:
                    user = project.manager
                
                TimeEntry.objects.create(
                    task=task,
                    user=user,
                    date=entry_date,
                    hours=hours,
                    description=f"Work on {task.title}"
                )
                print(f"Created time entry: {hours} hours on {entry_date} by {user.username}")

print("Project sample data creation completed!")
