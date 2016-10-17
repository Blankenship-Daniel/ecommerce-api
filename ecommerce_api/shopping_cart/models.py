from __future__ import unicode_literals

from django.db import models
from products.models import Product
from django.contrib.auth.models import User

class ShoppingCart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE
    )
    products = models.ManyToManyField(Product)

    def __unicode__(self):
        return self.user.username + "'s shopping cart"

class ShoppingCartProductQty(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
