# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_optica_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optica',
            name='image',
            field=models.ImageField(null=True, upload_to='images_opticas', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images_products', verbose_name='Imagen'),
        ),
    ]