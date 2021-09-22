from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm
from users.models import User

from products.models import ProductsCategory, Product
from admins.forms import CategoryForm

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


def index(request):
    return render(request, 'admins/admin.html')


class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser)
# def admin_users(request):
#     context = {
#         'users': User.objects.all()
#     }
#     return render(request, 'admins/admin-users-read.html', context)


class UserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Регистрация'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminRegisterForm()
#     context = {
#         'title': 'GeekShop - Aдмин | Регистрация',
#         'form': form
#     }
#     return render(request, 'admins/admin-users-create.html', context)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Обновление пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)



# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_update(request, id):
#     users_select = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, instance=users_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=users_select)
#     context = {
#         'title': 'GeekShop - Админ | Обновление пользователя',
#         'form': form,
#         'users_select': users_select
#     }
#     return render(request, 'admins/admin-users-update-delete.html', context)

class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_delete(request, id):
#     user = User.objects.get(id=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admins:admin_users'))





@user_passes_test(lambda u: u.is_superuser)
def admin_products_category(request):
    context = {
        'products_category': ProductsCategory.objects.all()
    }
    return render(request, 'admins/admin-products-category.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_category_create(request):
    if request.method == 'POST':
        form = CategoryForm(data=request.POST)
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


@user_passes_test(lambda u: u.is_superuser)
def admin_products_category_update(request, id):
    category_select = ProductsCategory.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryForm(data=request.POST, instance=category_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products_category'))
    else:
        form = CategoryForm(instance=category_select)
    context = {
        'title': 'GeekShop - Админ | Обновление категорий',
        'form': form,
        'category_select': category_select
    }
    return render(request, 'admins/admin-products-category-update-delete.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_category_delete(request, id):
#     user = User.objects.get(id=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admins:admin_products_category'))







@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'admins/admin-products.html', context)