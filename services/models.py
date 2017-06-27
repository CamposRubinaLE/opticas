# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
from accounts.models import User


class Optica(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='opticas/images', verbose_name='Imagen')
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name='Dirección')
    url = models.URLField(verbose_name='Link')
    owner = models.ForeignKey(User, related_name='opticas', verbose_name='Propietario')

    def __str__(self):
        return self.name
