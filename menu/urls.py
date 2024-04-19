from django.urls import path
from .views import GetOrders

urlpatterns = [
    path('foods/', GetOrders.as_view(), name='order-list')
]
