from django.db import models


class AvailableSubscription(models.Model):
    url_of_feed = models.URLField()
    feed_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.feed_name}"
