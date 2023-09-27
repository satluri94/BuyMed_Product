import random
import string
from django.shortcuts import render

from . import serializers
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework import viewsets
from .serializers import CartItemSerializer, StockSerializer
from .models import CartItem
from rest_framework.decorators import api_view
from .models import Stock
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class ListCartItems(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

@api_view(['POST'])
def addCartItem(request):
    if request.method == 'POST':
        new_cart_data = JSONParser().parse(request)
        product_title = new_cart_data['title']
        product_price = new_cart_data['price']
        if product_title is not None and product_price is not None:
            items = CartItem.objects.all()
            item = items.filter(title=product_title)
            if(item is not None):
                serializer = None
                serializer = CartItemSerializer(data=new_cart_data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                return JsonResponse({'message': 'Product already exists!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'One of the fields is empty!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def addStockItem(request):
    if request.method == 'POST':
        new_stock_data = JSONParser().parse(request)
        Med_title = new_stock_data['title']
        Med_price = new_stock_data['price']
        Med_cat = new_stock_data['category']
        if Med_title is not None and Med_price is not None and Med_cat is not None :
            items = Stock.objects.all()
            item = items.filter(title=Med_title)
            if(item is not None):
                serializer = None
                serializer = StockSerializer(data=new_stock_data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({'message': 'Item already exists!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'One of the fields is empty!'}, status=status.HTTP_204_NO_CONTENT)
        

class CategoryItems(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'title']

