from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images')
    created = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
