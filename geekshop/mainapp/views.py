import os.path

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
import json

from django.conf import settings
from django.core.cache import cache
from django.views.decorators.cache import cache_page, never_cache

from django.views.generic import DetailView

from mainapp.models import ProductCategory, Product

MODULE_DIR = os.path.dirname(__file__)


def get_link_category():
    if settings.LOW_CACHE:
        key = 'link_category'
        link_category = cache.get(key)
        if link_category is None:
            link_category = ProductCategory.objects.all()
            cache.set(key, link_category)
        return link_category
    else:
        return ProductCategory.objects.all()

# Create your views here.

def get_link_product():
    if settings.LOW_CACHE:
        key = 'link_product'
        link_product = cache.get(key)
        if link_product is None:
            link_product = Product.objects.all().select_related('category')
            cache.set(key, link_product)
        return link_product
    else:
        return Product.objects.all().select_related('category')

def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product{pk}'
        product = cache.get(key)
        if product is None:
            product = Product.objects.get(id=pk)
            cache.set(key, product)
        return product
    else:
        return Product.objects.get(id=pk)

def index(request):
    context = {
        'title': 'geekshop',
        'header': 'Добро пожаловать на сайт'
    }
    return render(request, 'mainapp/index.html', context)

# @cache_page(3600)
# @never_cache
def products(request, id_category=None, page=1):
    title = 'Geekshop | Каталог'

    if id_category:
        products = Product.objects.filter(category_id=id_category).select_related('category')
    else:
        products = Product.objects.all().select_related('category')

    products = get_link_product()

    paginator = Paginator(products, per_page=3)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    # categories = ProductCategory.objects.all()
    categories = get_link_category()
    context = {'title': title,
               'products': products_paginator,
               'categories': categories}

    return render(request, 'mainapp/products.html', context)


def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    title = 'Geekshop | Описание товара'

    context = {'title': title,
               'product': product,
    }

    return render(request, 'mainapp/detail.html', context)


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        # product = self.get_object()

        context['product'] = get_product(self.kwargs.get('pk'))
        # context['categories'] = get_link_category()
        return context