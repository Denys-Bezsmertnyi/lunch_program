from unittest import TestCase

from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from api.restaurants.api import RestaurantCreateView
from apps.restaurants.models import Restaurant, Menu
from datetime import date

class RestaurantCreateViewTestCase(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = RestaurantCreateView.as_view()
        self.url = '/api/restaurant/'

    def test_create_restaurant(self):
        data = {
            'name': 'Test Restaurant',
            'address': '123 Test Street',
            'restaurant_type': 'Fast Food'
        }

        request = self.factory.post(self.url, data, format='json')
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(Restaurant.objects.get().name, 'Test Restaurant')


class MenuCreateViewTests(APITestCase):

    def setUp(self):
        self.restaurant = Restaurant.objects.create(name='Test Restaurant')
        self.url = '/api/restaurant/menu/'

    def test_create_menu(self):
        data = {
            'restaurant': self.restaurant.id,
            'date': date.today(),
            'items': '["Burger", "Fries", "Drink"]'
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 1)
        self.assertEqual(Menu.objects.get().restaurant, self.restaurant)


class CurrentDayMenuViewTests(APITestCase):

    def setUp(self):
        self.restaurant = Restaurant.objects.create(name='Test Restaurant')
        self.url = f'/api/restaurant/current-menu/{self.restaurant.id}/'

    def test_get_current_day_menu(self):
        menu = Menu.objects.create(restaurant=self.restaurant, date=date.today(), items='["Salad", "Soup"]')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_no_menu_for_today(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['message'], 'Menu for today is not available')