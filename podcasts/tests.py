from django.http import request
from django.shortcuts import render
from django.test import TestCase,Client
from django.urls.base import reverse
from django.utils import timezone
from .models import Episode
import pytest
import conftest



@pytest.mark.django_db
def test_episode_content(creating_object):
    assert creating_object.description == "Look mom, I made it!"
    assert creating_object.link == "https://myawesomeshow.com"
    assert creating_object.guid == "de194720-7b4c-49e2-a05f-432436d3fetr"

@pytest.mark.django_db
def test_episode_str_representation(creating_object):
    assert str(creating_object) == "My Python Podcast: My Awesome Podcast Episode"

@pytest.mark.django_db
def test_home_page_status_code(creating_object):
    client = Client()
    response = client.get("/")
    assert response.status_code == 200

# @pytest.mark.django_db
# def test_home_page_uses_correct_template():
#     client = Client()
#     response = render(request,'homepage.html').
#     # print(response.content_type)
#     assert response == "homepage.html"

# @pytest.mark.django_db
# def test_homepage_list_contents(creating_object):
#     client = Client()
#     response = client.get(reverse("homepage"))
#     assert g == "My Awesome Podcast Episode"



# Create your tests here.
