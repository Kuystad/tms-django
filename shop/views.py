from django.shortcuts import render, get_object_or_404
from .models import Product, Category


# Create your views here.

def products_view(request):
    context = {'products': Product.objects.all()}
    return render(request, 'shop/products.html', context)


def product_detail(request, product_id: int):
    context = {'product': get_object_or_404(Product, id=product_id)}
    return render(request, 'shop/product_detail.html', context)


def categories_view(request):
    context = {'categories': Category.objects.all()}
    return render(request, 'shop/categories.html', context)


def category_detail(request, category_id: int):
    context = {'category': get_object_or_404(Category, id=category_id)}
    return render(request, 'shop/category_detail.html', context)


