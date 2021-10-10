from rest_framework import serializers
from .models import *




class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Collection
        fields = '__all__'


