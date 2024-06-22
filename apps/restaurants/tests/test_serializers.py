from django.test import TestCase
from apps.restaurants.models import Restaurant
from api.restaurants.serializers import RestaurantSerializer, MenuSerializer
from datetime import date


class RestaurantSerializerTest(TestCase):

    def setUp(self):
        self.restaurant_data = {
            'name': 'Test Restaurant',
            'address': 'Test Street',
            'restaurant_type': 'Fast Food',
        }

    def test_valid_data(self):
        serializer = RestaurantSerializer(data=self.restaurant_data)
        self.assertTrue(serializer.is_valid())
        restaurant = serializer.save()

        self.assertEqual(restaurant.name, self.restaurant_data['name'])
        self.assertEqual(restaurant.address, self.restaurant_data['address'])
        self.assertEqual(restaurant.restaurant_type, self.restaurant_data['restaurant_type'])

    def test_missing_name(self):
        data = self.restaurant_data.copy()
        del data['name']
        serializer = RestaurantSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)

    def test_blank_address(self):
        data = self.restaurant_data.copy()
        data['address'] = ''
        serializer = RestaurantSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('address', serializer.errors)


class MenuSerializerTest(TestCase):

    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name='Test Restaurant',
            address='123 Test Street',
            restaurant_type='Fast Food'
        )
        self.menu_data = {
            'restaurant': self.restaurant.id,
            'date': date.today(),
            'items': '["Burger", "Fries", "Drink"]'
        }

    def test_valid_data(self):
        serializer = MenuSerializer(data=self.menu_data)
        self.assertTrue(serializer.is_valid())
        menu = serializer.save()

        self.assertEqual(menu.restaurant.id, self.menu_data['restaurant'])
        self.assertEqual(menu.date, self.menu_data['date'])
        self.assertEqual(menu.items, self.menu_data['items'])

    def test_missing_items(self):
        data = self.menu_data.copy()
        del data['items']
        serializer = MenuSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('items', serializer.errors)

    def test_invalid_date_format(self):
        data = self.menu_data.copy()
        data['date'] = '2023-06-22'  # Invalid format, should be date object
        serializer = MenuSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('date', serializer.errors)
