# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
