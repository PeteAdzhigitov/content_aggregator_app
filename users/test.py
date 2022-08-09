import datetime
import logging
import os
from django.conf import settings
from django.core.management.base import BaseCommand
import feedparser
from dateutil import parser
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
import smtplib
from django.core.management.base import BaseCommand
from email.message import EmailMessage
from podcasts.models import Episode
from dateutil import parser
import feedparser

logger = logging.getLogger(__name__)
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
msg = EmailMessage()
#
# def send_email():
#     msg['To'] = 'adzhigitovpetr@gmail.com'
#     msg['From'] = EMAIL_ADDRESS
#     msg['Subject'] = 'New content for subscribers'
#     with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
#         smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
#         feed = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/World.xml")
#         data = []
#         for i in feed.entries:
#             if parser.parse(i.item.published) > datetime.datetime(2022,7,21,23,0,0):
#                 data.append(i.item.title)
#             msg.set_content(f'{data[0]}, {data[1]} and many more interesting news')
#             smtp.send_message(msg)
# def main():
#     send_email()
#
# if "__name__" == '__main__':
#     main()



feed = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/World.xml")
for i in feed.entries:
    if parser.parse(i.item.published) > datetime.datetime(2022,7,21,23,0,0):
        print("Hello")
        break

# podcast_title = feed.channel.title
# podcast_image = feed.channel.image["href"]


# proper_date = parser.parse(i.channel.pubDate)