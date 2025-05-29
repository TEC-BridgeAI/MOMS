# backend/apps/hr/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['name']
    search_fields = ['name', 'description']

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['department', 'position', 'hire_date']
    search_fields = ['employee_id', 'user__first_name', 'user__last_name', 'position']
