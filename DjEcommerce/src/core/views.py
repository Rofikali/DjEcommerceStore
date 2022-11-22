from django.shortcuts import render, get_object_or_404
from core.models import Product, Category


def home(request):
    product = Product.objects.all()
    category = Category.objects.all()
    context = {
        'product': product,
        'category': category
    }
    return render(request, 'core/home.html', context)


def detail_view(request, slug):
    data = get_object_or_404(Product, slug=slug)
    images = Product.objects.all()
    context = {
        'data': data,
        'images': images
    }
    return render(request, 'core/detail.html', context)
