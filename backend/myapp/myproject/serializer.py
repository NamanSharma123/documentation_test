from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self,value):
        if value < 0:
            raise serializers.ValidationError("Price must be 0 or positive")
        return value
    
    def validate_stock(self,value):
        if value < 0:
            raise serializers.ValidationError("Stock must be 0 or positive")
        return value
