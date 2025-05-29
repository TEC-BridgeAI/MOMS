# backend/apps/finance/serializers.py
from rest_framework import serializers
from .models import Account, Transaction, TransactionLine, Invoice, InvoiceItem

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class TransactionLineSerializer(serializers.ModelSerializer):
    account_name = serializers.ReadOnlyField(source='account.name')
    
    class Meta:
        model = TransactionLine
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    lines = TransactionLineSerializer(many=True, read_only=True)
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Transaction
        fields = '__all__'

class InvoiceItemSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    
    class Meta:
        model = InvoiceItem
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True, read_only=True)
    total_amount = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    customer_name = serializers.ReadOnlyField(source='customer.name')
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Invoice
        fields = '__all__'
