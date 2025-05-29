# backend/apps/crm/views.py
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Count
from .models import Customer, Contact, Opportunity, Activity
from .serializers import CustomerSerializer, ContactSerializer, OpportunitySerializer, ActivitySerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['customer_type', 'assigned_to']
    search_fields = ['name', 'email', 'phone']
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    @action(detail=True, methods=['get'])
    def activities(self, request, pk=None):
        customer = self.get_object()
        activities = Activity.objects.filter(customer=customer)
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['customer', 'is_primary']
    search_fields = ['first_name', 'last_name', 'email', 'phone']

class OpportunityViewSet(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['customer', 'status', 'assigned_to']
    search_fields = ['name', 'description']
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        stats = {
            'total_value': Opportunity.objects.aggregate(total=Sum('amount'))['total'] or 0,
            'by_status': Opportunity.objects.values('status').annotate(
                count=Count('id'),
                value=Sum('amount')
            ).order_by('status')
        }
        return Response(stats)

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['customer', 'opportunity', 'activity_type', 'completed']
    search_fields = ['subject', 'description']
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
