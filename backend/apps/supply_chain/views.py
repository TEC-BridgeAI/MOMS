# backend/apps/supply_chain/views.py
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Count
from django.utils import timezone
from .models import Supplier, Product, PurchaseOrder, PurchaseOrderItem
from .serializers import SupplierSerializer, ProductSerializer, PurchaseOrderSerializer, PurchaseOrderItemSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['name', 'contact_name', 'email', 'phone']
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['supplier']
    search_fields = ['name', 'sku', 'description']
    
    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        products = Product.objects.filter(current_stock__lt=models.F('min_stock_level'))
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def update_stock(self, request, pk=None):
        product = self.get_object()
        if 'quantity' in request.data:
            product.current_stock += int(request.data['quantity'])
            product.save()
            return Response({'current_stock': product.current_stock, 'stock_status': product.stock_status})
        return Response({'error': 'quantity is required'}, status=400)

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['supplier', 'status']
    search_fields = ['order_number', 'notes']
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    @action(detail=True, methods=['post'])
    def receive(self, request, pk=None):
        purchase_order = self.get_object()
        if purchase_order.status == 'shipped':
            purchase_order.status = 'received'
            purchase_order.delivery_date = timezone.now().date()
            purchase_order.save()
            
            # Update product stock levels
            for item in purchase_order.items.all():
                product = item.product
                product.current_stock += item.quantity
                product.save()
            
            return Response({'status': 'Purchase order received and stock updated'})
        return Response({'error': 'Purchase order must be in shipped status'}, status=400)

class PurchaseOrderItemViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['purchase_order', 'product']
