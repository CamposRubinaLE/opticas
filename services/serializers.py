from rest_framework import serializers
from .models import Product

__author__ = 'lucaru9'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image', 'url', 'price']
