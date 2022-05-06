from django.urls import re_path as url
from InventaryApp import views

urlpatterns=[
    url(r'^product$',views.productApi),
    url(r'^product/([0-9]+)$',views.productApi),
    url(r'^listproducts$',views.listProductsApi)
]