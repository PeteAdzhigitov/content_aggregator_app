from django.urls import path
from .views import HomePageView, SubscriptionListView


urlpatterns = [
    path('homepage',HomePageView.as_view(),name='homepage'),
    path('homepage/subscriptions',SubscriptionListView.as_view(),name='subscriptions'),
]