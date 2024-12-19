from rest_framework.serializers import ModelSerializer
from .models import *

class AdvertiseSerializer(ModelSerializer):
    class Meta:
        model = Advertise
        fields='__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['brand']=instance.brand.name
        representation['cars_type']=instance.cars_type.name
        representation['category']=instance.category.name
        representation['author']=instance.author.email
        representation['country']=instance.country.name


        return representation

class BrandsSerializer(ModelSerializer):
    class Meta:
        model = Brands
        fields='__all__'

class CarsCountrySerializer(ModelSerializer):
    class Meta:
        model=Country
        fields='name'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields='__all__'

class AuthorSerializer(ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['id', 'email']

class CountrySerializer(ModelSerializer):
    class Meta:
        model=Country
        fields='__all__'

