from rest_framework import serializers
from .models import BillingInfo, ShippingInfo

class BillingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingInfo
        fields = ('user', 'street1', 'street2', 'city', 'state') 

class ShippingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingInfo
        fields = ('user', 'street1', 'street2', 'city', 'state')
