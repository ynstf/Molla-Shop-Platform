from base.models import Category,Product
from django.contrib.auth.models import User

categories = Category.objects.all()
products = Product.objects.all()

products.delete()
categories.delete()
