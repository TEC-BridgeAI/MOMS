# backend/apps/finance/views.py
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from django.utils import timezone
from .models import Account, Transaction, TransactionLine, Invoice, InvoiceItem
from .serializers import AccountSerializer, TransactionSerializer, TransactionLineSerializer, InvoiceSerializer, InvoiceItemSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['account_type', 'parent']
    search_fields = ['name', 'code', 'description']

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['status', 'date', 'created_by']
    search_fields = ['reference', 'description']
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    @action(detail=True, methods=['post'])
    def post_transaction(self, request, pk=None):
        transaction = self.get_object()
        if transaction.status == 'draft':
            transaction.status = 'posted'
            transaction.save()
            return Response({'status': 'Transaction posted'})
        return Response({'status': 'Transaction cannot be posted'}, status=400)

class TransactionLineViewSet(viewsets.ModelViewSet):
    queryset = TransactionLine.objects.all()
    serializer_class = TransactionLineSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['transaction', 'account']

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['customer', 'status', 'date', 'due_date']
    search_fields = ['invoice_number', 'notes']
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    @action(detail=False, methods=['get'])
    def overdue(self, request):
        today = timezone.now().date()
        overdue = Invoice.objects.filter(due_date__lt=today, status='sent')
        serializer = self.get_serializer(overdue, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def summary(self, request):
        summary = {
            'total_invoiced': Invoice.objects.aggregate(total=Sum('items__quantity', field='items__quantity*items__unit_price'))['total'] or 0,
            'total_paid': Invoice.objects.filter(status='paid').aggregate(total=Sum('items__quantity', field='items__quantity*items__unit_price'))['total'] or 0,
            'total_overdue': Invoice.objects.filter(status='overdue').aggregate(total=Sum('items__quantity', field='items__quantity*items__unit_price'))['total'] or 0,
        }
        return Response(summary)

class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['invoice']
