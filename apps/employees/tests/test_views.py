import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_create_employee(api_client):
    url = reverse('employee-list')
    data = {
        'username': 'testuser',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'testuser@example.com',
        'phone_number': '+380123456789',
        'age': 30,
        'gender': 'M',
        'password': 'password123'
    }

    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_employee_detail(api_client):
    user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password123')
    url = reverse('employee-detail', kwargs={'pk': user.pk})

    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['username'] == 'testuser'