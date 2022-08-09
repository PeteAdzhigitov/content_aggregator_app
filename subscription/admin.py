from django.contrib import admin
from .models import AvailableSubscription

# Register your models here.
@admin.register(AvailableSubscription)
class AvailableSubscriptionAdmin(admin.ModelAdmin):
    list_display = ("feed_name","url_of_feed")




