# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billinginfo',
            name='street2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='shippinginfo',
            name='street2',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
