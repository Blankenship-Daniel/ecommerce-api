from __future__ import unicode_literals

from django.db import models
from products.models import Product

class ShoppingCart(models.Model):
    products = models.ManyToManyField(Product)
