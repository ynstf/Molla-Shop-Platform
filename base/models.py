from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="categories_images/", default='/static/default_category.png')
    
    def __str__(self):
        return self.category_name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()

    """def promo(self):
        return self.price"""
    #promotion = models.FloatField()

    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to="products_images/",default='/static/default_product.png')


    def __str__(self):
        return self.name

class Rate(models.Model):
    product = models.OneToOneField(Product,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    rate = models.IntegerField()


    def __str__(self):
        return self.product.name

