from django.urls import path
from .views import product_view

app_name = 'products'

urlpatterns = [
    path("product/", product_view, name='product')
]
