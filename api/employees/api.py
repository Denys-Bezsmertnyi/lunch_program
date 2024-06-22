from rest_framework import generics, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import EmployeeRegistrationSerializer, CustomTokenObtainPairSerializer, EmployeeSerializer
from apps.employees.models import Employee
from rest_framework.permissions import AllowAny


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.none()  # Empty queryset because we only allow creation
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]  # Allow any user to create an employee

    def get_queryset(self):
        return Employee.objects.none()  # Return empty queryset for other actions

    def perform_create(self, serializer):
        serializer.save()  #


class EmployeeRegistrationView(generics.CreateAPIView):
    serializer_class = EmployeeRegistrationSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
