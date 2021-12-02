from django.urls import path

from admins.views import index
from baskets.views import basket_add, basket_remove, basket_edit

app_name = 'admins'
urlpatterns = [
    path('', index, name='index'),

]
