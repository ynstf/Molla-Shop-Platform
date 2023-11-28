from django.shortcuts import render, redirect
import json
from .forms import RegisterForm, ProductForm
from django.contrib import messages
from .models import Product, Category
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
import requests
import os

# Create your views here.
def home(request):
    title = "MOLLA - Home"

    #q = request.GET.get("q") if request.GET.get("q") != None else ''
    search = request.GET.get("search") if request.GET.get("search") != None else ''
    #print(search)

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
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            url = f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/api/register"
            myobj = {
                "username":username,
                "email":email,
                "password":password
                    }
            x = requests.post(url, json = myobj)
            #form.save()
            #print(int(x.content))
            if int(x.content) == 1 :
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


def Login(request):
    title = "Login"
    categories = Category.objects.all()
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        url = f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/api/login"
        myobj = {
            "username":username,
            "password":password
                }
        x = requests.post(url, json = myobj)
        #if user true
        if int(json.loads(x.content.decode('utf8'))['login']) == 1 :
            #return home page
            #messages.success(request, 'welcome')
            token = json.loads(x.content.decode('utf8'))['jwt']
            response = redirect("home")
            response.set_cookie(key='jwt', value=token, httponly=True)
            #set jwt cookie
            url = f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/api/user"
            token = {'jwt':request.COOKIES.get('jwt')}
            x = requests.get(url,data=token)
            #login with user
            #user = User.objects.get(username=json.loads(x.content.decode('utf8'))['username'])
            user_to_log = authenticate(username=username,password=password)
            login(request,user_to_log)
            
            return response
        # if user false
        elif int(json.loads(x.content.decode('utf8'))['login']) == 0 :
            errors = json.loads(x.content.decode('utf8'))['error']
            return render(request,'base/login.html',{'errors':errors})

    context = {
        "title":title,
        "categories":categories,
    }

    return render(request,'base/login.html',context)


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
                #print(i)
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

def Logout(request):

    response = redirect("home")
    response.delete_cookie('sessionid')
    response.delete_cookie('jwt')
    return response
