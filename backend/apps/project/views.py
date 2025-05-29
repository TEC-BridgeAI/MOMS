# backend/apps/project/views.py
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Count
from django.utils import timezone
from .models import Project, Task, TimeEntry, Milestone
from .serializers import ProjectSerializer, TaskSerializer, TimeEntrySerializer, MilestoneSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['status', 'manager', 'members']
    search_fields = ['name', 'description']
    
    def perform_create(self, serializer):
        project = serializer.save(created_by=self.request.user)
        project.members.add(self.request.user)
    
    @action(detail=True, methods=['get'])
    def tasks(self, request, pk=None):
        project = self.get_object()
        tasks = Task.objects.filter(project=project)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def stats(self, request, pk=None):
        project = self.get_object()
        stats = {
            'total_tasks': project.tasks.count(),
            'completed_tasks': project.tasks.filter(status='done').count(),
            'total_hours': TimeEntry.objects.filter(task__project=project).aggregate(total=Sum('hours'))['total'] or 0,
            'by_status': project.tasks.values('status').annotate(count=Count('id')).order_by('status'),
        }
        return Response(stats)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['project', 'status', 'priority', 'assigned_to']
    search_fields = ['title', 'description']
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    @action(detail=False, methods=['get'])
    def my_tasks(self, request):
        tasks = Task.objects.filter(assigned_to=request.user).exclude(status='done')
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

class TimeEntryViewSet(viewsets.ModelViewSet):
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['task', 'user', 'date']
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MilestoneViewSet(viewsets.ModelViewSet):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['project', 'completed', 'due_date']
    search_fields = ['title', 'description']
