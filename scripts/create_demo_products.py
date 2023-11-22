from base.models import Category,Product
from django.contrib.auth.models import User
from random import choice


prods = ["prod1","prod2","prod3","phone","TV","PC"]

caties = ["Daily offers","Gift Ideas","Beds","Lighting","Sofas & Sleeper sofas","Storage","Armchairs & Chaises","Decoration" ,"Kitchen Cabinets","Coffee & Tables","Outdoor Furniture"]

for i in range(len(caties)):
    category0 = Category.objects.create(category_name=caties[i])
    category0.save()

for i in range(10):
    user = User.objects.get(username='root')
    product = Product.objects.create(user= user,name= choice(prods) ,short_description = "",description = "",price = 30,information = "",shipping_roles = "",)
    product.category.add(Category.objects.get(category_name=choice(caties)))
    product.save()


