from django.urls import path, include
from .api import RestaurantCreateView, MenuCreateView, CurrentDayMenuView, RestaurantMenuListView

urlpatterns = [
    path('', RestaurantCreateView.as_view()),
    path('menu/', MenuCreateView.as_view()),
    path('current-menu/<int:restaurant_id>/', CurrentDayMenuView.as_view(), name='current-menu'),
    path('current-day/', RestaurantMenuListView.as_view(), name='current-day'),
]