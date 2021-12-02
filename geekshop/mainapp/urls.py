from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('<int:pk>/', mainapp.products, name='category'),
    #path('detail/<int:product_id>/', mainapp.detail, name='detail'),
    path('detail/<int:pk>/', mainapp.ProductDetail.as_view(), name='detail'),
]