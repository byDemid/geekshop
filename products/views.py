from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
import json

from django.views.generic import DetailView

from products.models import Product, ProductsCategory

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.


def index(request):
    context = {
        'title': 'geekbrains',
    }
    return render(request, 'products/index.html', context)


def products(request, id=None, page=1):

    products = Product.objects.filter(category_id=id) if id != None else Product.objects.all()
    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    # if id != None:
    #     products_filter = Product.objects.filter(category_id=id)
    # else:
    #     products_filter = Product.objects.all()

    context = {'title': 'Каталог',
               'categories': ProductsCategory.objects.all(),
               }
    context['products'] = products_paginator

    # context['products'] = products_filter
    # context.update({'products': Product.objects.filter(category_id=id) if id != None else Product.objects.all()})

    return render(request, 'products/products.html', context)

class ProductDetail(DetailView):

    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, category_id=None, *args, **kwargs):
        context = super().get_context_data()
        context['categories'] = ProductsCategory.objects.all()
        return context
