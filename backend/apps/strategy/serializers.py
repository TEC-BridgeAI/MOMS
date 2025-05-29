# backend/apps/strategy/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import StrategicPlan, Goal, Objective, KeyResult

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class KeyResultSerializer(serializers.ModelSerializer):
    progress = serializers.FloatField(read_only=True)
    
    class Meta:
        model = KeyResult
        fields = '__all__'

class ObjectiveSerializer(serializers.ModelSerializer):
    key_results = KeyResultSerializer(many=True, read_only=True)
    progress = serializers.SerializerMethodField()
    
    class Meta:
        model = Objective
        fields = '__all__'
    
    def get_progress(self, obj):
        key_results = obj.key_results.all()
        if not key_results:
            return 0
        return sum(kr.progress for kr in key_results) / key_results.count()

class GoalSerializer(serializers.ModelSerializer):
    objectives = ObjectiveSerializer(many=True, read_only=True)
    responsible_name = serializers.ReadOnlyField(source='responsible.username')
    progress = serializers.SerializerMethodField()
    
    class Meta:
        model = Goal
        fields = '__all__'
    
    def get_progress(self, obj):
        objectives = obj.objectives.all()
        if not objectives:
            return 0
        return sum(self.fields['objectives'].child.get_progress(objective) for objective in objectives) / objectives.count()

class StrategicPlanSerializer(serializers.ModelSerializer):
    goals = GoalSerializer(many=True, read_only=True)
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    progress = serializers.SerializerMethodField()
    
    class Meta:
        model = StrategicPlan
        fields = '__all__'
    
    def get_progress(self, obj):
        goals = obj.goals.all()
        if not goals:
            return 0
        return sum(self.fields['goals'].child.get_progress(goal) for goal in goals) / goals.count()
