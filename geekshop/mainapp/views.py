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


def products(request):
    title = 'Geekshop | Каталог'
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    context = {'title': title,
               'products': products,
               'categories': categories}
    # with open('mainapp/fixtures/products_old.json', 'r', encoding="utf-8") as f:
    #     context = json.load(f)

    # context = {
    #     'title': 'geekshop - каталог',
    #     'header': 'Добро пожаловать на сайт',
    #     'products': [
    #         {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090,
    #          'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
    #          'href':'vendor/img/products/Adidas-hoodie.png'},
    #         {'name': 'Синяя куртка The North Face', 'price': 23725,
    #          'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
    #          'href':'vendor/img/products/Blue-jacket-The-North-Face.png'},
    #         {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390,
    #          'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
    #          'href':'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
    #         {'name': 'Черный рюкзак Nike Heritage', 'price': 2340, 'description': 'Плотная ткань. Легкий материал.',
    #          'href':'vendor/img/products/Black-Nike-Heritage-backpack.png'},
    #         {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590,
    #          'description': 'Гладкий кожаный верх. Натуральный материал.',
    #          'href':'vendor/img/products/Black-Dr-Martens-shoes.png'},
    #         {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890,
    #          'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
    #          'href':'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'}
    #     ]
    # }
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