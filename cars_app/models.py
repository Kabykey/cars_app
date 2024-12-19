from django.db import models
from django.contrib.auth.models import BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if email is None:
            raise ValueError('Email is required')
        email=self.normalize_email(email)
        user=self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        user = self.create_user(email, password, **extra_fields)
        return user

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

class Advertise(models.Model):
    name=models.CharField(max_length=255)
    brand=models.ForeignKey('Brands', on_delete=models.PROTECT)
    cars_type=models.ForeignKey('Cars_type', on_delete=models.PROTECT)
    category=models.ForeignKey('Category', on_delete=models.PROTECT)
    country=models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
    description=models.TextField(max_length=900)
    car_price = models.PositiveIntegerField()
    author=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    years=models.PositiveIntegerField()

    def __str__(self):
        return str(self.brand) + ' ' + str(self.cars_type)+ ' ' +str(self.car_price)+''+'Tenge'

class Brands(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Country(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Cars_type(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

