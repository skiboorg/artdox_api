from rest_framework import serializers
from .models import *
from Item.serializers import ItemSerializer
class CartSerializer(serializers.ModelSerializer):


    items = ItemSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Cart
        fields = '__all__'





