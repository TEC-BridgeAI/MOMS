# backend/apps/crm/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer, Contact, Opportunity, Activity

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Activity
        fields = '__all__'

class OpportunitySerializer(serializers.ModelSerializer):
    assigned_to_name = serializers.ReadOnlyField(source='assigned_to.username')
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    customer_name = serializers.ReadOnlyField(source='customer.name')
    activities = ActivitySerializer(many=True, read_only=True)
    
    class Meta:
        model = Opportunity
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, read_only=True)
    opportunities = OpportunitySerializer(many=True, read_only=True)
    assigned_to_name = serializers.ReadOnlyField(source='assigned_to.username')
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Customer
        fields = '__all__'
