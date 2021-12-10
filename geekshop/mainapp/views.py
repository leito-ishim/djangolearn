from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
import json

from django.views.generic import DetailView

from .models import ProductCategory, Product


# Create your views here.


def index(request):
    context = {
        'title': 'geekshop',
        'header': 'Добро пожаловать на сайт'
    }
    return render(request, 'mainapp/index.html', context)


def products(request, id_category=None, page=1):
    title = 'Geekshop | Каталог'

    if id_category:
        products = Product.objects.filter(category_id=id_category)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, per_page=3)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    categories = ProductCategory.objects.all()
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
        product = self.get_object()
        context['product'] = product
        return context