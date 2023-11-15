from django.shortcuts import render
from .models import Product

products = [
    {"id":1, "name":"iphone pro max 15"},
    {"id":2, "name":"gun to kill your enemy"},
    {"id":3, "name":"coka and marejuana"},
        ]

# Create your views here.
def home(request):
    title = "Home"
    products = Product.objects.all()


    context = {
        "title":title,
        "products":products,
    }
    return render(request,"base/home.html",context)

def product(request,pk):
    product = Product.objects.get(pk=pk)
    title = product.name
    categories = product.category.all()
    

    
    context = {
        "title":title,
        "product":product,
        "categories":categories,
        }
    return render(request,"base/product.html",context)