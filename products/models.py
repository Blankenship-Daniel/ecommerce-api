from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    price = models.FloatField()
    imageUrl = models.URLField()

    class Meta:
        ordering = ('created',)
