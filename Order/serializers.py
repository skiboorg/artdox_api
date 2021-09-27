from rest_framework import serializers
from .models import *
from Item.serializers import ItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'





