from django.urls import path, include
from .api import EmployeeRegistrationView, CustomTokenObtainPairView, EmployeeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employees')


urlpatterns = [
    path('signup/', EmployeeRegistrationView.as_view()),
    path('login/', CustomTokenObtainPairView.as_view()),
    path('', include(router.urls)),
]