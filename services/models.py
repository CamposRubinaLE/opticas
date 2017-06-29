# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from accounts.models import User


class District(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Distrito'
        verbose_name_plural = 'Distritos'
        ordering = ['-created_at']


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
    district = models.ForeignKey(District, related_name='opticas', verbose_name='Distrito', null=True)

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
    stock = models.PositiveIntegerField(verbose_name='Stock', null=True)
    optica = models.ForeignKey(Optica, related_name='products', verbose_name='Óptica', null=True)
    category = models.ForeignKey(Category, related_name='products', verbose_name='Categoría')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-created_at']


class Promotion(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=500, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='images_promotions', verbose_name='Imagen')
    url = models.URLField(verbose_name='Link')
    is_enable = models.BooleanField(default=True, verbose_name='Habilitada')
    optica = models.ForeignKey(Optica, related_name='promotions', verbose_name='Óptica', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Promoción'
        verbose_name_plural = 'Promociones'
        ordering = ['-created_at']
