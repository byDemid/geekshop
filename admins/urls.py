# """geekshop URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
#
# app_name = 'admins'
#
# from .views import index, UserListView, UserCreateView, UserUpdateView, UserDeleteView, admin_products_category_update,\
#     admin_products_category_delete, admin_products_create, admin_products_update, admin_products_delete
# # admin_users, admin_users_create, admin_users_update, admin_users_delete
# from .views import admin_products_category, admin_products, admin_products_category_create
#
# urlpatterns = [
#     path('', index, name='index'),
#     path('users/', UserListView.as_view(), name='admin_users'),
#     path('user-create/', UserCreateView.as_view(), name='admin_users_create'),
#     path('user-update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
#     path('user-delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),
#
#     path('products-category/', admin_products_category, name='admin_products_category'),
#     path('products-category-create/', admin_products_category_create, name='admin_products_category_create'),
#     path('products-category-update/<int:id>', admin_products_category_update, name='admin_products_category_update'),
#     path('products-category-delete/<int:id>', admin_products_category_delete, name='admin_products_category_delete'),
#
#     path('products/', admin_products, name='admin_products'),
#     path('products-create/', admin_products_create, name='admin_products_create'),
#     path('admin-products-update/<int:id>', admin_products_update, name='admin_products_update'),
#     path('admin-products-delete/<int:id>', admin_products_delete, name='admin_products_delete'),
# ]

from django.contrib import admin
from django.urls import path

app_name = 'admins'

from .views import index, UserDeleteView, UserUpdateView, UserCreateView, UserListView, CategoryListView, \
    CategoryDeleteView, CategoryUpdateView, ProductListView, CategoryCreateView, ProductCreateView, ProductUpdateView

# admin_users , admin_users_create,admin_users_update,admin_users_delete

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('user-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('user-update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('user-delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),

    path('category/', CategoryListView.as_view(), name='admin_category'),
    path('category-delete/<int:pk>/', CategoryDeleteView.as_view(), name='admin_category_delete'),
    path('category-update/<int:pk>/', CategoryUpdateView.as_view(), name='admin_category_update'),
    # path('category-detail/<int:pk>/', CategoryDetailView.as_view(), name='admin_category_detail'),
    path('category-create/', CategoryCreateView.as_view(), name='admin_products_category_create'),

    path('product/', ProductListView.as_view(), name='admin_product'),
    path('product-create/', ProductCreateView.as_view(), name='admin_products_create'),
    path('product-update/<int:pk>/', ProductUpdateView.as_view(), name='admin_product_update'),
]
