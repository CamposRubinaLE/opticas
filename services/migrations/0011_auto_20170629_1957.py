# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-29 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_promotion_is_enable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='name',
            field=models.CharField(max_length=500, verbose_name='Nombre'),
        ),
    ]
