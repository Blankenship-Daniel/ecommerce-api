from django.contrib import admin

from .models import ShippingInfo, BillingInfo

admin.site.register(ShippingInfo)
admin.site.register(BillingInfo)
