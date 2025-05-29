# backend/sample_collaboration_data.py
import os
import django
import random
from datetime import datetime, timedelta

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moms_project.settings')
django.setup()

# Import models
from django.contrib.auth.models import User
from apps.collaboration.models import Team, TeamMember, Document, Comment

# Clear existing collaboration data
print("Clearing existing collaboration data...")
Comment.objects.all().delete()
Document.objects.all().delete()
TeamMember.objects.all().delete()
Team.objects.all().delete()
print("Existing collaboration data cleared.")

# Get users for assigning ownership
users = User.objects.all()
if not users:
    print("No users found. Please run the HR data script first.")
    exit()

# Create teams
teams = [
    {"name": "Product Development", "description": "Team responsible for product development and innovation"},
    {"name": "Marketing Team", "description": "Team handling marketing campaigns and brand management"},
    {"name": "Sales Team", "description": "Team focused on sales and customer acquisition"},
    {"name": "Executive Committee", "description": "Leadership team overseeing company strategy"},
    {"name": "IT Support", "description": "Technical support and infrastructure management team"}
]

created_teams = []
for team_data in teams:
    # Select a random user as team creator
    created_by = random.choice(users)
    
    team = Team.objects.create(
        name=team_data["name"],
        description=team_data["description"],
        created_by=created_by
    )
    created_teams.append(team)
    print(f"Created team: {team.name}")
    
    # Add creator as admin
    TeamMember.objects.create(
        team=team,
        user=created_by,
        role='admin'
    )
    
    # Add 3-6 random members to the team
    team_size = random.randint(3, 6)
    potential_members = list(users)
    potential_members.remove(created_by)  # Remove creator as they're already added
    
    if len(potential_members) > 0:
        # Select random members (up to available users)
        num_members = min(team_size, len(potential_members))
        team_members = random.sample(potential_members, num_members)
        
        for user in team_members:
            role = random.choice(['admin', 'member', 'guest'])
            TeamMember.objects.create(
                team=team,
                user=user,
                role=role
            )
            print(f"Added {user.username} to {team.name} as {role}")

# Create documents for each team
document_templates = [
    {"title": "Project Plan", "content": "This document outlines the project plan including timeline, resources, and deliverables."},
    {"title": "Meeting Minutes", "content": "Minutes from the team meeting held on {date}, discussing project progress and next steps."},
    {"title": "Quarterly Goals", "content": "Team objectives and key results for Q{quarter} {year}."},
    {"title": "Team Charter", "content": "This charter defines the team's purpose, values, and operating guidelines."},
    {"title": "Budget Proposal", "content": "Proposed budget for the upcoming fiscal year with breakdown of expenses and justifications."}
]

for team in created_teams:
    # Get team members
    team_members = User.objects.filter(teammember__team=team)
    
    # Create 3-5 documents per team
    num_docs = random.randint(3, 5)
    for i in range(num_docs):
        # Select a random document template
        doc_template = random.choice(document_templates)
        
        # Format dynamic content
        current_date = datetime.now()
        content = doc_template["content"].format(
            date=current_date.strftime("%B %d, %Y"),
            quarter=((current_date.month-1)//3)+1,
            year=current_date.year
        )
        
        # Select a random team member as document creator
        if team_members:
            created_by = random.choice(team_members)
        else:
            created_by = team.created_by
        
        document = Document.objects.create(
            title=f"{doc_template['title']} - {team.name}",
            content=content,
            team=team,
            created_by=created_by
        )
        print(f"Created document: {document.title}")
        
        # Add 0-5 comments to the document
        num_comments = random.randint(0, 5)
        for j in range(num_comments):
            # Select a random team member as commenter
            if team_members:
                commenter = random.choice(team_members)
            else:
                commenter = team.created_by
                
            comment_text = random.choice([
                "Great document, thanks for sharing!",
                "I have some suggestions for this section.",
                "Can we discuss this at the next meeting?",
                "This looks good to me.",
                "I've updated my part of this document.",
                "Please review my changes when you get a chance."
            ])
            
            Comment.objects.create(
                document=document,
                user=commenter,
                text=comment_text
            )
            print(f"Added comment to {document.title} by {commenter.username}")

print("Collaboration sample data creation completed!")
