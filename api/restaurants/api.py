from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.restaurants.models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date


class RestaurantCreateView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]



class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]


class CurrentDayMenuView(APIView):
    def get(self, request, restaurant_id):
        today = date.today()
        try:
            menu = Menu.objects.get(restaurant_id=restaurant_id, date=today)
            serializer = MenuSerializer(menu)
            return Response(serializer.data)
        except Menu.DoesNotExist:
            return Response({"message": "Menu for today is not available"}, status=404)


class RestaurantMenuListView(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        current_date = date.today()

        menus = Menu.objects.filter(date=current_date)

        return menus
