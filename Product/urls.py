from django.urls import path
from .views import ListCartItems, CategoryItems
from . import views

urlpatterns = [
    path('cartitem/add/', views.addCartItem, name='cart_items'),
    path('cartitems/', ListCartItems.as_view(), name='get_cartItems'),
    # path('cartitem/remove/', views.removeCartItem, name='cart_items'),
    path('stockitem/add/', views.addStockItem, name='stock_items'),
    path('stockitems/', CategoryItems.as_view(), name='get_stockItems'),
    # path('stockitem/remove/', views.removeCartItem, name='cart_items'),
]