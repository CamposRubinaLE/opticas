from django.conf.urls import url
from .views import ListProductAPI

__author__ = 'lucaru9'

urlpatterns = [
    url(r'^api/v1/products/', ListProductAPI.as_view()),

]
