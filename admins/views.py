from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm
from users.models import User

from products.models import ProductsCategory, Product
from admins.forms import CategoryForm

# Create your views here.


def index(request):
    return render(request, 'admins/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'GeekShop - Aдмин | Регистрация',
        'form': form
    }
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, id):
    users_select = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, instance=users_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=users_select)
    context = {
        'title': 'GeekShop - Админ | Обновление пользователя',
        'form': form,
        'users_select': users_select
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_products_category(request):
    context = {
        'products_category': ProductsCategory.objects.all()
    }
    return render(request, 'admins/admin-products-category.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'admins/admin-products.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_category_create(request):
    if request.method == 'POST':
        form = CategoryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products_category'))
    else:
        form = CategoryForm()
    context = {
        'title': 'GeekShop - Aдмин | Создание категории',
        'form': form
    }
    return render(request, 'admins/admin-products-category-create.html', context)