from django.urls import path, include

urlpatterns = [
    path('auth/', include('api.employees.urls')),
    path('restaurant/', include('api.restaurants.urls')),
]