from django.urls import path
from .views import calculate_fare_api, fare_calculator_page

urlpatterns = [
    path('calculate_fare/', calculate_fare_api, name='calculate_fare'),
    path('fare_calculator/', fare_calculator_page, name='fare_calculator_page'),
]
