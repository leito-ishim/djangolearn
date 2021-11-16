from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'geekshop',
        'header': 'Добро пожаловать на сайт'
    }
    return render(request, 'index.html', context)


def products(request):
    context = {
        'title': 'geekshop продукты',
        'header': 'Добро пожаловать на сайт',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090,
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'href':'/static/vendor/img/products/Adidas-hoodie.png'},
            {'name': 'Синяя куртка The North Face', 'price': 23725,
             'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'href':'/static/vendor/img/products/Blue-jacket-The-North-Face.png'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390,
             'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'href':'/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340, 'description': 'Плотная ткань. Легкий материал.',
             'href':'/static/vendor/img/products/Black-Nike-Heritage-backpack.png'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590,
             'description': 'Гладкий кожаный верх. Натуральный материал.',
             'href':'/static/vendor/img/products/Black-Dr-Martens-shoes.png'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890,
             'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'href':'/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'}
        ]
    }
    return render(request, 'products.html', context)
