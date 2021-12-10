from django.urls import path

from admins.views import index, UserListView, UserUpdateView, UserDeleteView, UserCreateView
from admins.views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from admins.views import ProductListView,ProductCreateView,ProductUpdateView,ProductDeleteView

app_name = 'admins'
urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),

    path('categories/', CategoryListView.as_view(), name='admin_categories'),
    path('categories_create/', CategoryCreateView.as_view(), name='admin_categories_create'),
    path('categories_update/<int:pk>/', CategoryUpdateView.as_view(), name='admin_categories_update'),
    path('categories_delete/<int:pk>/', CategoryDeleteView.as_view(), name='admin_categories_delete'),

    path('products/', ProductListView.as_view(), name='admin_products'),
    path('products_create/', ProductCreateView.as_view(), name='admin_products_create'),
    path('products_update/<int:pk>/', ProductUpdateView.as_view(), name='admin_products_update'),
    path('products_delete/<int:pk>/', ProductDeleteView.as_view(), name='admin_products_delete'),
]
