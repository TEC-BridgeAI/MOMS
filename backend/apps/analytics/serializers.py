# backend/apps/analytics/serializers.py
from rest_framework import serializers
from .models import Dashboard, Report

class ReportSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Report
        fields = '__all__'

class DashboardSerializer(serializers.ModelSerializer):
    reports = ReportSerializer(many=True, read_only=True)
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Dashboard
        fields = '__all__'
