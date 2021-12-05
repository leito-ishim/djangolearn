from django.contrib import admin
from .models import ProductCategory,Product

# Register your models here.
#admin.site.register(Product)
admin.site.register(ProductCategory)


@admin.register(Product)
class Product(admin.ModelAdmin):

    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name','description', ('price', 'quantity'), 'category')