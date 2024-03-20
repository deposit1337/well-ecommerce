from django.db import models


# Create your models here.
# from django.utils.text import slugify

from django.db import models
from django.utils.text import slugify


# Categories of products
class Category(models.Model):
    name = models.CharField(max_length=20)
    brand_name_1 = models.CharField(max_length=50)
    brand_name_2 = models.CharField(max_length=50)
    quantity_1 = models.IntegerField(default=1)
    quantity_2 = models.IntegerField(default=1)

    image = models.ImageField(upload_to='uploads/product/',default='uploads/product/defualt.png')
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    brand_name = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name='products_category')
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    full_name_decs = models.CharField(max_length=100,default='')

    image = models.ImageField(upload_to='uploads/product/',default='well_ecom/media/uploads/product/default.png')

    def __str__(self):
        return self.brand_name


class ProductImages(models.Model):
    product = models.ForeignKey(Product,related_name='images',on_delete=models.CASCADE)
    image_1 = models.ImageField(upload_to='uploads/product/product-decs/',default='well_ecom/media/uploads/product/default.png')
    image_2 = models.ImageField(upload_to='uploads/product/product-decs/',
                                default='well_ecom/media/uploads/product/default.png')
    image_3 = models.ImageField(upload_to='uploads/product/product-decs/',
                                default='well_ecom/media/uploads/product/default.png')