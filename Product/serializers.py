from rest_framework import serializers
from .models import CartItem, Stock


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [ 'title', 'price']

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['title', 'price', 'category', 'description']
