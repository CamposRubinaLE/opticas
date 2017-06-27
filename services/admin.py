# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Optica, Category, Product, StoreHouse


class OpticaAdmin(admin.ModelAdmin):
    model = Optica
    exclude = ['owner', ]
    list_display = ['name', 'owner', 'created_at', 'url']

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()


admin.site.register(Optica, OpticaAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(StoreHouse)
