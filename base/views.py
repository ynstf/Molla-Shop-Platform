from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from .models import Product


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

def register(request):
    title = "Create an Account"
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are registered successfully, please login to your account')
            return redirect("home")
    else:
        form = RegisterForm()


    context = {
        "title":title,
        "form":form
    }
    return render(request, "base/register.html", context)



