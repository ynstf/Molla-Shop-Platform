from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .models import Category

urlpatterns = [
    path("", views.home, name='home'),
    path("product/<str:pk>/", views.product, name='product'),
    path("listing/", views.listing, name='listing'),
    path("register/", views.register, name="register"),
    path("login/", views.Login, name="login"),
    #path("login/", auth_views.LoginView.as_view(extra_context={'title': 'Login',"categories" : Category.objects.all()},template_name = 'base/login.html'), name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("policy/", views.policy, name="policy"),
    #path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("logout/", views.Logout , name="logout"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
