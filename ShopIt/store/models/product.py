from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default = 100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , default=1 )
    desc = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='uploads/products/')


    def get_all_products():
        return Product.objects.all()

    def get_all_product_by_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()