# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import RedirectView

from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Product, Category, District, Promotion
from .serializers import ProductSerializer, CategorySerializer, DistrictSerializer, PromotionSerializer
from .filters import ProductFilter


class ListProductAPI(ListAPIView):
    ''' Filtro: {{Dominio}}/api/v1/products/?category=2&category=1&name=nombre&min_price=&max_price=&district=

    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProductFilter


class ListCategoryAPI(ListAPIView):
    ''' Lista Categorias para el filtro de productos ['id','name'], Se pueden elegir varias categorias

    '''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()
    pagination_class = None


class ListDistrictAPI(ListAPIView):
    ''' Lista Distritos

    '''
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()
    pagination_class = None


class ListPromotionAPI(ListAPIView):
    ''' Lista Promociones

    '''
    queryset = Promotion.objects.filter(is_enable=True)
    serializer_class = PromotionSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()
