from django.shortcuts import render

import os
import json

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.


def index(request):
    context = {
        'title': 'geekbrains',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'каталог'}

    path_category = os.path.join(MODULE_DIR, 'fixtures/category.json')
    context['categories'] = open(path_category, mode='r', encoding='UTF-8')

    # path_file = os.path.join(MODULE_DIR, 'fixtures/products.json')

    path_goods = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context['products'] = open(path_goods, mode='r', encoding='UTF-8')

    return render(request, 'products/products.html', context)
