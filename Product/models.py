from django.db import models
# from django.contrib.auth.models import Product
import os


class CartItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=20, blank=False)

class Stock(models.Model):
    title = models.CharField(max_length=50, blank=False, default='', primary_key=True)
    price = models.CharField(max_length=20, blank=False)
    category = models.CharField(max_length=40, blank=False)
    description = models.CharField(max_length=100, blank=False)
