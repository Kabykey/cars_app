from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from cars_app.models import *
from .serializers import *
class AdvertiseApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        advertises= Advertise.objects.all()
        data = AdvertiseSerializer(instance=advertises, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        new_advertise = AdvertiseSerializer(data=request.data)
        if new_advertise.is_valid():
            new_advertise.save()
            return Response({'message':'Your advertise has been created'}, status=status.HTTP_200_OK)
        else:
            return Response(new_advertise.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        advertise_id=request.data.get('id')
        if advertise_id is None:
            return Response({'message':'Field ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        from django.shortcuts import get_object_or_404
        advertise = get_object_or_404(Advertise, id=advertise_id)
        updated_advertise = AdvertiseSerializer(instance=advertise, data=request.data, partial=True)
        if updated_advertise.is_valid():
            updated_advertise.save()
            return Response(data={'message': 'OK!'}, status=status.HTTP_200_OK)
        return Response(data=updated_advertise.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        advertise_id=request.data.get('id')
        if advertise_id is None:
            return Response(data={'message': 'Please enter ID'}, status=status.HTTP_400_BAD_REQUEST)
        from django.shortcuts import get_object_or_404
        advertise = get_object_or_404(Advertise, id=advertise_id)
        advertise.delete()
        return Response(data={'message':'Your advertise has been deleted'}, status=status.HTTP_200_OK)


class BrandsByTypeApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        cars_type = request.GET.get('cars_type')
        cars = Advertise.objects.filter(cars_type=cars_type)
        data = AdvertiseSerializer(instance=cars, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)



class CarsFilterApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        cars_type=request.GET.get('cars_type')
        cars_year=request.GET.get('years')
        cars_country=request.GET.get('country')
        min_price=request.GET.get('min_price')
        max_price=request.GET.get('max_price')

        cars=Advertise.objects.all()
        if cars_type is not None:
            cars = cars.filter(cars_type=cars_type)
        if cars_year is not None:
            cars = cars.filter(years=cars_year)
        if cars_country is not None:
            cars =cars.filter(country=cars_country)
        if min_price is not None:
            cars=cars.filter(car_price__gte=min_price)
        if max_price is not None:
            cars=cars.filter(car_price__lte=max_price)

        data = AdvertiseSerializer(instance=cars, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

class CategoryApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        category=request.GET.get('category')
        category=Category.objects.all()
        data=CategorySerializer(instance=category, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)



# class
class AuthorsApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        advertise=Advertise.objects.filter(author=request.user)
        data=AdvertiseSerializer(instance=advertise, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    def patch(self, request):
        advertise_id=request.data.get('id')
        if advertise_id is None:
            return Response({'message':'Field ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        from django.shortcuts import get_object_or_404
        advertise = get_object_or_404(Advertise, id=advertise_id)
        updated_advertise = AdvertiseSerializer(instance=advertise, data=request.data, partial=True)
        if updated_advertise.is_valid():
            updated_advertise.save()
            return Response(data={'message': 'OK!'}, status=status.HTTP_200_OK)
        return Response(data=updated_advertise.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        request.user.delete()
        return Response(data={'message': 'Delete!'}, status=status.HTTP_200_OK)


class CountryApiView(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        country=request.GET.get('country')
        country=Country.objects.all()
        data=CategorySerializer(instance=country, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        country = CountrySerializer(data=request.data)

        if country.is_valid():
            country.save()
            return Response(data={'message': 'OK!'}, status=status.HTTP_200_OK)
        return Response(data=country.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        from django.contrib.auth import authenticate, login
        email=request.data.get('email')
        if email is None:
            return Response(data={'message':'please enter your email'}, status=status.HTTP_400_BAD_REQUEST)
        password=request.data.get('password')
        if password is None:
            return Response(data={'message':'Please filed password'},status=status.HTTP_400_BAD_REQUEST)

        user=authenticate(email=email, password=password)

        if user is None:
            return Response(data={'message':'Incorrect username and/or password'}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)
        return Response(data={'message':'Welcome'}, status=status.HTTP_200_OK)

class RegistrationApiView(APIView):
    def post(self,request):
        email=request.data.get('email')
        if email is None:
            return Response(data={'message':'Please enter email'}, status=status.HTTP_400_BAD_REQUEST)
        password=request.data.get('password')
        if password is None:
            return Response(data={'message':'Please enter password'}, status=status.HTTP_400_BAD_REQUEST)
        password1=request.data.get('password1')
        if password !=password1:
            return Response(data={'message': 'Password and Password1 not match!'}, status=status.HTTP_400_BAD_REQUEST)

        CustomUser.objects.create_user(email=email, password=password)
        return Response(data={'message': 'User Created!'}, status=status.HTTP_200_OK)

class UserCabinetApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = AuthorSerializer(instance=request.user, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)

    def patch(self, request):
        user = AuthorSerializer(instance=request.user, data=request.data, partial=True)
        if user.is_valid():
            user.save()
            return Response(data=user.data, status=status.HTTP_200_OK)
        return Response(data=user.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        request.user.delete()
        return Response(data={'message': 'Delete!'}, status=status.HTTP_200_OK)

class CarsApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        import requests
        response = requests.get('https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/all-vehicles-model/records?limit=20')
        cars = response.json()
        data = {
            'name': cars['results'][0]['make'],
            'model': cars['results'][0]['model'],
            'class': cars['results'][0]['vclass']
        }
        return Response(data=data, status=status.HTTP_200_OK)

class AdvertiseSearchApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, reguest):
        name = reguest.GET.get('name')
        if name is None:
            adv=Advertise.objects.all()
        else:
            adv=Advertise.objects.filter(name__icontains=name)
        data=AdvertiseSerializer(instance=adv, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

from rest_framework.pagination import PageNumberPagination


class AdvPaginatedApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        all_advertise = Advertise.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 1
        advertise = paginator.paginate_queryset(all_advertise, request)
        data = AdvertiseSerializer(instance=advertise, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)