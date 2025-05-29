# backend/apps/analytics/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Dashboard, Report
from .serializers import DashboardSerializer, ReportSerializer

class DashboardViewSet(viewsets.ModelViewSet):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['created_by']
    search_fields = ['name', 'description']
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['dashboard', 'report_type', 'created_by']
    search_fields = ['title', 'description']
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    @action(detail=True, methods=['get'])
    def data(self, request, pk=None):
        report = self.get_object()
        # In a real implementation, this would execute the query and return data
        # This is a simplified example
        sample_data = {
            'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
            'datasets': [
                {
                    'label': 'Sample Data',
                    'data': [65, 59, 80, 81, 56]
                }
            ]
        }
        return Response(sample_data)
