from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class BillingInfo(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        primary_key = True
    )
    street1 = models.CharField(max_length=100)
    street2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10, default="00000-0000")

class ShippingInfo(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        primary_key = True
    )
    street1 = models.CharField(max_length=100)
    street2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10, default="00000-0000")
