# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
from accounts.models import User


class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created_at']


class Optica(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='images_opticas', verbose_name='Imagen', null=True)
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name='Dirección')
    url = models.URLField(verbose_name='Link')
    owner = models.ForeignKey(User, related_name='opticas', verbose_name='Propietario')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Óptica'
        verbose_name_plural = 'Ópticas'
        ordering = ['-created_at']


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='images_products', verbose_name='Imagen')
    url = models.URLField(verbose_name='Link')
    price = models.PositiveIntegerField(verbose_name='Precio')
    category = models.ForeignKey(Category, related_name='products', verbose_name='Categoría')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-created_at']


class StoreHouse(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField(verbose_name='Stock')
    product = models.ForeignKey(Product, related_name='storehouses', verbose_name='Producto')
    optica = models.ForeignKey(Optica, related_name='storehouses', verbose_name='Óptica')

    def __str__(self):
        return 'Óptica: {}  --  Producto:  {} -- Stock:  {}'.format(self.optica, self.product, self.stock)

    class Meta:
        verbose_name = 'Almacén'
        verbose_name_plural = 'Almacenes'
        ordering = ['-created_at']
        unique_together = ('product', 'optica')
