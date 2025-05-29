# backend/apps/compliance/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Policy, Regulation, ComplianceTask, Audit

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class PolicySerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Policy
        fields = '__all__'

class RegulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regulation
        fields = '__all__'

class ComplianceTaskSerializer(serializers.ModelSerializer):
    assigned_to_name = serializers.ReadOnlyField(source='assigned_to.username')
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    policy_title = serializers.ReadOnlyField(source='policy.title')
    regulation_name = serializers.ReadOnlyField(source='regulation.name')
    
    class Meta:
        model = ComplianceTask
        fields = '__all__'

class AuditSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Audit
        fields = '__all__'
