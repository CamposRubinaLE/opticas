# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Optica, Category, Product, Promotion, District


class OpticaAdmin(admin.ModelAdmin):
    model = Optica
    exclude = ['owner', ]
    list_display = ['name', 'owner', 'created_at', 'url']

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(OpticaAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)


class PromotionAdmin(admin.ModelAdmin):
    model = Promotion
    list_display = ['optica', 'name', 'is_enable']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "optica":
            kwargs["queryset"] = Optica.objects.filter(owner=request.user)
        return super(PromotionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super(PromotionAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(optica__owner=request.user)


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'optica', 'category', 'url']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "optica":
            kwargs["queryset"] = Optica.objects.filter(owner=request.user)
        return super(ProductAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(optica__owner=request.user)


admin.site.register(Optica, OpticaAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Promotion, PromotionAdmin)
admin.site.register(District)
