from django.contrib import admin

from .models import ShoppingCart, ShoppingCartProductQty

admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartProductQty)
