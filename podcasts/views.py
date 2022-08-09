from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Episode, Subscription
from django.views.generic import ListView
from django.contrib.auth.models import User
# Create your views here.


class HomePageView(ListView):
    model = Episode
    template_name = 'homepage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["episodes"] = Episode.objects.filter(is_published=True).order_by("-pub_date")
        return context

class SubscriptionListView(ListView):
    template_name = 'subscription.html'
    context_object_name = 'subscriptions'

    def get_queryset(self):
        current_user = self.request.user
        return Subscription.objects.filter(user=current_user)

