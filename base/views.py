from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import ProductForm
from django.contrib import messages
from .models import Product, Category
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    title = "MOLLA - Home"

    #q = request.GET.get("q") if request.GET.get("q") != None else ''
    search = request.GET.get("search") if request.GET.get("search") != None else ''
    print(search)

    #products = Product.objects.all()
    #products = Product.objects.filter(category__category_name__icontains=q)
    products = Product.objects.filter(
        Q(name__contains=search) | 
        Q(description__contains=search) |
        Q(category__category_name__icontains=search)
        )
    
    categories = Category.objects.all()
    


    context = {
        "title":title,
        "products":products,
        "categories":categories,
    }
    return render(request,"base/home.html",context)

def product(request,pk):
    product = Product.objects.get(pk=pk)
    title = product.name
    categories_of_product = product.category.all()
    categories = Category.objects.all()
    

    
    context = {
        "title":title,
        "product":product,
        "categories_of_product":categories_of_product,
        "categories":categories,
        }
    return render(request,"base/product.html",context)

def register(request):
    title = "Create an Account"
    categories = Category.objects.all()
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
        "form":form,
        "categories":categories,
    }
    return render(request, "base/register.html", context)


@login_required
def listing(request):
    title = 'add new product'
    categories = Category.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            catigories_id= dict(request.POST.lists())["category"]
            new_product = form.save(commit = False)
            new_product.user = request.user
            new_product.save()
            for i in catigories_id:
                print(i)
                c = Category.objects.get(pk=i)
                new_product.category.add(c)

            messages.success(request, 'The product has been created successfully')
            return redirect("home")
    else:
        form = ProductForm()

    context = {
        "title":title,
        "product_form":form,
        "categories":categories,
    }
    return render(request, "base/listing.html", context)


@login_required
def dashboard(request):
    title = 'MOLLA - dashboard'



    context = {
        "title":title,
    }
    return render(request, "base/dashboard.html", context)


def policy(request):
    title = 'MOLLA - Policy'



    context = {
        "title":title,
    }
    return render(request, "base/policy.html", context)


