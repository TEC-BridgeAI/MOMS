# backend/apps/project/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, Task, TimeEntry, Milestone

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'

class TimeEntrySerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = TimeEntry
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    assigned_to_name = serializers.ReadOnlyField(source='assigned_to.username')
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    time_entries = TimeEntrySerializer(many=True, read_only=True)
    total_hours = serializers.SerializerMethodField()
    
    class Meta:
        model = Task
        fields = '__all__'
    
    def get_total_hours(self, obj):
        return sum(entry.hours for entry in obj.time_entries.all())

class ProjectSerializer(serializers.ModelSerializer):
    manager_name = serializers.ReadOnlyField(source='manager.username')
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    members_count = serializers.SerializerMethodField()
    tasks_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = '__all__'
    
    def get_members_count(self, obj):
        return obj.members.count()
    
    def get_tasks_count(self, obj):
        return obj.tasks.count()
