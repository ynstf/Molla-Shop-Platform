from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import Product


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProductForm(forms.ModelForm):
    #image = forms.ImageField(default='static/default_product.png')
    class Meta:
        model = Product
        fields = ["name",
                "short_description", 
                "description",
                "price",
                "information",
                "shipping_roles",
                "category",
                "image",
                "product_side",
                "product_cross",
                "product_with_model",
                "product_back",
                ]


