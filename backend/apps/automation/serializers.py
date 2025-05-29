# backend/apps/automation/serializers.py
from rest_framework import serializers
from .models import Workflow, Task, Schedule

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class WorkflowSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    schedules = ScheduleSerializer(many=True, read_only=True)
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Workflow
        fields = '__all__'
