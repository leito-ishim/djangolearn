from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=64, verbose_name='название категории', unique=True)
    description = models.TextField(verbose_name='Описание раздела товаров', blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='название продукта,товара')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание товара, продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='Описание товара, продукта', blank=True, null=True)
    price = models.DecimalField(verbose_name='стоимость продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество товара', default=0)

    def __str__(self):
        return f'{self.name} ({self.category.name})'