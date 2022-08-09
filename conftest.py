import pytest
from django.utils import timezone

from podcasts.models import Episode


@pytest.fixture
def creating_object():
    episode = Episode.objects.create(
    title="My Awesome Podcast Episode",
    description="Look mom, I made it!",
    pub_date=timezone.now(),
    link="https://myawesomeshow.com",
    image="https://image.myawesomeshow.com",
    podcast_name="My Python Podcast",
    guid="de194720-7b4c-49e2-a05f-432436d3fetr",)

    return episode


