from django.shortcuts import render

import os
import json

from products.models import Product, ProductsCategory

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.


def index(request):
    context = {
        'title': 'geekbrains',
    }
    return render(request, 'products/index.html', context)


def products(request):
    # context = {'title': 'Каталог'}
    # path_file = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    # context['products'] = json.load(open(path_file, encoding='UTF-8'))
    context = {'title': 'Каталог',
               'products': Product.objects.all(),
               'categories': ProductsCategory.objects.all(),
               }
    return render(request, 'products/products.html', context)
