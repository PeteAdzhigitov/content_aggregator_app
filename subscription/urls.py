
from django.urls import path
from .views import all_available_subscriptions

urlpatterns = [
    path('homepage/available_subscriptions',all_available_subscriptions ,name='available_subscriptions'),
]