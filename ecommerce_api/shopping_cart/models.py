from __future__ import unicode_literals

from django.db import models
from products.models import Product
from django.contrib.auth.models import User

class ShoppingCart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        primary_key = True
    )
    products = models.ManyToManyField(Product, through='ShoppingCartProduct')

class ShoppingCartProduct(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart)
    product = models.ForeignKey(Product)
    qty = models.IntegerField()
