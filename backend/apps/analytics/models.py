# backend/apps/analytics/models.py
from django.db import models
from django.contrib.auth.models import User

class Dashboard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dashboards')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Report(models.Model):
    REPORT_TYPES = (
        ('bar', 'Bar Chart'),
        ('line', 'Line Chart'),
        ('pie', 'Pie Chart'),
        ('table', 'Table'),
        ('kpi', 'KPI'),
    )
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name='reports')
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    query = models.TextField(help_text="SQL query or data source configuration")
    config = models.JSONField(default=dict, help_text="Report configuration in JSON format")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
