from django.conf.urls import url

from .views import ListProductAPI, ListDistrictAPI, ListCategoryAPI, ListPromotionAPI

__author__ = 'lucaru9'

urlpatterns = [
    url(r'^api/v1/promotions/', ListPromotionAPI.as_view()),
    url(r'^api/v1/products/', ListProductAPI.as_view()),
    url(r'^api/v1/districts/', ListDistrictAPI.as_view()),
    url(r'^api/v1/categories/', ListCategoryAPI.as_view()),
]
