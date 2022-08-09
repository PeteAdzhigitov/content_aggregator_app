from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Episode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    podcast_name = models.CharField(max_length=100)
    guid = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.podcast_name}: {self.title}"

class Subscription(models.Model):
    feed_url = models.URLField()
    subcription_name = models.CharField(max_length=200)
    is_subscribed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)

    def __str__(self):
        return f'{self.subcription_name}: {self.is_subscribed}'

