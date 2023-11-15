from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="categories_images/", default='../static/default_category.png')
    
    def __str__(self):
        return self.category_name

class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=255)
    short_description = models.TextField()
    description = models.TextField(null=True,blank=True)
    price = models.FloatField()
    information = models.TextField(null=True,blank=True)
    shipping_roles = models.TextField(null=True,blank=True)

    """def promo(self):
        return self.price"""
    #promotion = models.FloatField()

    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to="products_images/",default='../static/default_product.png')
    product_side = models.ImageField(upload_to="products_images/",default='../static/default_product.png')
    product_cross = models.ImageField(upload_to="products_images/",default='../static/default_product.png')
    product_with_model = models.ImageField(upload_to="products_images/",default='../static/default_product.png')
    product_back = models.ImageField(upload_to="products_images/",default='../static/default_product.png')

    def __str__(self):
        return self.name

class Rate(models.Model):
    product = models.OneToOneField(Product,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    rate = models.IntegerField()


    def __str__(self):
        return self.product.name

