from django.shortcuts import render
from .models import Product


def product_view(request):
    context = {
        'product': Product.objects.all()
    }
    return render(request, 'product/product.html', context)
