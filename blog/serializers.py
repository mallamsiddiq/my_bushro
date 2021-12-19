from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Order



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_id', 'date_created', 'total_amount', 'status')
