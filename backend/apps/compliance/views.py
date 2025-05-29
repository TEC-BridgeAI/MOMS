# backend/apps/compliance/views.py
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Policy, Regulation, ComplianceTask, Audit
from .serializers import PolicySerializer, RegulationSerializer, ComplianceTaskSerializer, AuditSerializer

class PolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['status', 'created_by']
    search_fields = ['title', 'description', 'content']
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class RegulationViewSet(viewsets.ModelViewSet):
    queryset = Regulation.objects.all()
    serializer_class = RegulationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['authority']
    search_fields = ['name', 'description', 'authority']

class ComplianceTaskViewSet(viewsets.ModelViewSet):
    queryset = ComplianceTask.objects.all()
    serializer_class = ComplianceTaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['status', 'priority', 'assigned_to', 'policy', 'regulation']
    search_fields = ['title', 'description']
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    @action(detail=False, methods=['get'])
    def overdue(self, request):
        today = timezone.now().date()
        tasks = ComplianceTask.objects.filter(due_date__lt=today, status__in=['pending', 'in_progress'])
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

class AuditViewSet(viewsets.ModelViewSet):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['status', 'created_by']
    search_fields = ['title', 'description', 'findings']
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
