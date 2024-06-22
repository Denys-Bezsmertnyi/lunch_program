import pytest
from django.contrib.auth import get_user_model

import employee_lunch
from api.employees.serializers import EmployeeSerializer, EmployeeRegistrationSerializer

User = get_user_model()
DJANGO_SETTINGS_MODULE=employee_lunch.settings
@pytest.fixture
def sample_employee_data():
    return {
        'username': 'testuser',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'testuser@example.com',
        'phone_number': '+380123456789',
        'age': 30,
        'gender': 'M',
        'password': 'password123'
    }

def test_employee_serializer_create_valid(sample_employee_data):
    serializer = EmployeeSerializer(data=sample_employee_data)
    assert serializer.is_valid()

    employee = serializer.save()
    assert employee.username == sample_employee_data['username']

def test_employee_registration_serializer_save_valid(sample_employee_data):
    serializer = EmployeeRegistrationSerializer(data=sample_employee_data)
    assert serializer.is_valid()

    employee = serializer.save()
    assert employee.username == sample_employee_data['username']