from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.name
