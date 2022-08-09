from django.contrib import admin

# Register your models here.
from .models import Episode,Subscription

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ("podcast_name", "title", "pub_date")

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("feed_url", "subcription_name", "is_subscribed")