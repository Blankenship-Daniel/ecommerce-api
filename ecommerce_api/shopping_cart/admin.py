from django.contrib import admin

from .models import ShoppingCart, ShoppingCartProduct

admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartProduct)
