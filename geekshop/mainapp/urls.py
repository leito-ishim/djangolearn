from django.urls import path
from django.views.decorators.cache import cache_page

from mainapp.views import products, ProductDetail
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='products'),
    path('category/<int:id_category>/', cache_page(3600)(products), name='category'),
    path('page/<int:page>/', products, name='page'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail'),
]