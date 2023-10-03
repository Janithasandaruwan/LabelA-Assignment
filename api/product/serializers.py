from rest_framework import serializers
from .models import Product

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        # Model to be serialized
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method == 'GET':
            self.Meta.depth = 1
        else:
            self.Meta.depth = 0