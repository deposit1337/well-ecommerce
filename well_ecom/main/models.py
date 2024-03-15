from django.db import models


# Create your models here.


# Categories of products
class Category(models.Model):
    name = models.CharField(max_length=20)
    brand_name_1 = models.CharField(max_length=50)
    brand_name_2 = models.CharField(max_length=50)
    quantity_1 = models.IntegerField(default=1)
    quantity_2 = models.IntegerField(default=1)

    image = models.ImageField(upload_to='uploads/product/',default='well_ecom/media/uploads/product/default.png')

    def __str__(self):
        return self.name


class Product(models.Model):
    brand_name = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name='products_category')
    description = models.CharField(max_length=250, default='', blank=True, null=True)

    image = models.ImageField(upload_to='uploads/product/',default='well_ecom/media/uploads/product/default.png')

    def __str__(self):
        return self.brand_name
