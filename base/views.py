from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import ProductForm
from django.contrib import messages
from .models import Product
from django.contrib.auth.decorators import login_required

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


@login_required
def listing(request):
    title = 'add new product'

    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            new_product = form.save(commit = False)
            new_product.user = request.user
            new_product.save()

            messages.success(request, 'The product has been created successfully')
            return redirect("home")
    else:
        form = ProductForm()

    context = {
        "title":title,
        "product_form":form
    }
    return render(request, "base/listing.html", context)

