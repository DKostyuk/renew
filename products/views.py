from django.shortcuts import render
from products.models import *


def product(request, slug):
    print('999999999999999999999999   ', slug)
    product = Product.objects.get(slug=slug)
    products_big = Product.objects.filter(is_active=True, name_common=product.name_common)
    print(product.name_common)
    print(products_big)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    return render(request, 'products/product.html', locals())


def product_line(request, slug):
    # product = Product.objects.get(slug=slug)
    product_line = ProductCategory.objects.get(slug=slug)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True,
                                                  product__category__is_active=True, product__category__slug=slug)
    products_big = Product.objects.filter(is_active=True, category__is_active=True, category__slug=slug)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    return render(request, 'products/product_line.html', locals())
