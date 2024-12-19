"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cars_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('advertises', AdvertiseApiView.as_view()),
    path('cars_type', BrandsByTypeApiView.as_view()),
    path('cars_filter', CarsFilterApiView.as_view()),
    path('category', CategoryApiView.as_view()),
    path('authors', AuthorsApiView.as_view()),
    path('country', CountryApiView.as_view()),
    path('auth', AuthApiView.as_view()),
    path('registration', RegistrationApiView.as_view()),
    path('cab', UserCabinetApiView.as_view()),
    path('cars', CarsApiView.as_view()),
    path('search', AdvertiseSearchApiView.as_view()),
    path('paginator', AdvPaginatedApiView.as_view()),
]
