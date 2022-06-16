from dataclasses import field
from pyexpat import model
from orders.models import Order
from rest_framework import serializers 

class OrderSerializer(serializers.ModelSerializer):

    SIZE=(
        ('SMALL','small'),
        ('MEDIUM','medium'),
        ('LARGE','large')
    )
    size = serializers.ChoiceField(SIZE)

    quantity = serializers.IntegerField()

    class Meta:
        model=Order
        fields = ['id','size','quantity','order_status']
class OrderDetail_Serializer(serializers.ModelSerializer):

    SIZE=(
        ('SMALL','small'),
        ('MEDIUM','medium'),
        ('LARGE','large')
    )
    ORDER_STATUS = (
        ('PENDING','pending'),
        ('DELIVERING','delivering'),
        ('DELIVERED','delivered')
    )
    size = serializers.ChoiceField(SIZE)
    quantity = serializers.IntegerField()
    order_status = serializers.ChoiceField(ORDER_STATUS)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField() 

    class Meta:
        model=Order
        fields = ['id','size','quantity','order_status','created_at','updated_at']

class UpdateStatusSerializer(serializers.ModelSerializer):
    ORDER_STATUS = (
        ('PENDING','pending'),
        ('DELIVERING','delivering'),
        ('DELIVERED','delivered')
    )
    order_status = serializers.ChoiceField(ORDER_STATUS)
    class Meta:
        model=Order
        fields = ['order_status']