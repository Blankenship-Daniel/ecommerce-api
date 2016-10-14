from rest_framework import serializers
from .models import ShoppingCart, ShoppingCartProduct

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ('user', 'products') 

class ShoppingCartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartProduct
        fields = ('shopping_cart', 'product', 'qty')
