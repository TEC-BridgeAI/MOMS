# backend/apps/strategy/views.py
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count
from .models import StrategicPlan, Goal, Objective, KeyResult
from .serializers import StrategicPlanSerializer, GoalSerializer, ObjectiveSerializer, KeyResultSerializer

class StrategicPlanViewSet(viewsets.ModelViewSet):
    queryset = StrategicPlan.objects.all()
    serializer_class = StrategicPlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['status', 'created_by']
    search_fields = ['title', 'description']
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    @action(detail=True, methods=['get'])
    def summary(self, request, pk=None):
        plan = self.get_object()
        summary = {
            'total_goals': plan.goals.count(),
            'completed_goals': plan.goals.filter(status='completed').count(),
            'by_status': plan.goals.values('status').annotate(count=Count('id')).order_by('status'),
            'by_priority': plan.goals.values('priority').annotate(count=Count('id')).order_by('priority'),
        }
        return Response(summary)

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['strategic_plan', 'status', 'priority', 'responsible']
    search_fields = ['title', 'description']

class ObjectiveViewSet(viewsets.ModelViewSet):
    queryset = Objective.objects.all()
    serializer_class = ObjectiveSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['goal', 'status']
    search_fields = ['title', 'description']

class KeyResultViewSet(viewsets.ModelViewSet):
    queryset = KeyResult.objects.all()
    serializer_class = KeyResultSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['objective']
    search_fields = ['title', 'description']
    
    @action(detail=True, methods=['post'])
    def update_progress(self, request, pk=None):
        key_result = self.get_object()
        if 'current_value' in request.data:
            key_result.current_value = request.data['current_value']
            key_result.save()
            return Response({'progress': key_result.progress})
        return Response({'error': 'current_value is required'}, status=400)
