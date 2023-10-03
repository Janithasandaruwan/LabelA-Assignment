from rest_framework import serializers
from .models import Product

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        # Model to be serialized
        model = Product
        # Fields to be serialized 
        fields = ('id', 'name', 'description', 'price', 'stock', 'category')