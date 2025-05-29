# backend/apps/automation/models.py
from django.db import models
from django.contrib.auth.models import User

class Workflow(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('paused', 'Paused'),
        ('archived', 'Archived'),
    )
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workflows')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    TASK_TYPES = (
        ('email', 'Send Email'),
        ('notification', 'Send Notification'),
        ('api_call', 'API Call'),
        ('data_process', 'Process Data'),
        ('custom', 'Custom Script'),
    )
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('running', 'Running'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=100)
    task_type = models.CharField(max_length=20, choices=TASK_TYPES)
    config = models.JSONField(default=dict, help_text="Task configuration in JSON format")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.workflow.name} - {self.name}"

class Schedule(models.Model):
    FREQUENCY_CHOICES = (
        ('once', 'Once'),
        ('hourly', 'Hourly'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('custom', 'Custom Cron'),
    )
    
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='schedules')
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    cron_expression = models.CharField(max_length=100, blank=True, null=True)
    next_run = models.DateTimeField(blank=True, null=True)
    last_run = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.workflow.name} - {self.frequency}"
