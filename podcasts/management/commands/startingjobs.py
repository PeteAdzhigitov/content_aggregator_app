import datetime
import logging
import os

import pytz
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
from podcasts.models import Episode, Subscription
from datetime import datetime
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
msg = EmailMessage()

msg['From'] = EMAIL_ADDRESS
msg['Subject'] = 'New content for subscribers'
tz = pytz.timezone('Europe/Moscow')

def send_email():
    users = User.objects.all()
    for user in users:
        current_user = User.objects.get(id=user.id)
        user_email = current_user.email
        subscriptions = Subscription.objects.filter(user=current_user)
        # k = current_user.subscriptions_set.all()
        if len(subscriptions) == 0:
            pass
        else:
            for j in subscriptions:
                feed = feedparser.parse(j.feed_url)
                data = []
                time_restriction = datetime(2022, 8, 2, 12, 20, 0, 0, pytz.utc).astimezone(tz)
                for i in feed.entries:
                    if parser.parse(i.published) > time_restriction:
                        data.append(i.title)
                if len(data) >= 1:
                        msg['To'] = user_email
                        # msg.add_alternative("""\
                        # <!DOCTYPE html>
                        # <body>
                        # <h1><a href="http://127.0.0.1:8000/homepage">Click to find out</a></h1><br><br>
                        # </body>
                        # </html>
                        # """, subtype='html')
                        msg.set_content(f'{data[0]}' if len(
                            data) == 1 else f'"{data[0]},"\n"{data[1]} and many more interesting news"')
                        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                            smtp.send_message(msg)
                            smtp.quit()
                            del msg['To']
                else:
                    pass

# def update_available_subscription():
#     for i in scheduler.get_jobs():
#         i


def save_new_episodes(feed):
    """Saves new episodes to the database.

    Checks the episode GUID against the episodes currently stored in the
    database. If not found, then a new `Episode` is added to the database.

    Args:
        feed: requires a feedparser object
    """
    podcast_title = feed.channel.title
    podcast_image = feed.channel.image["href"]

    for item in feed.entries:
        if not Episode.objects.filter(guid=item.guid).exists():
            episode = Episode(
                title=item.title,
                description=item.description,
                pub_date=parser.parse(item.published),
                link=item.link,
                image=podcast_image,
                podcast_name=podcast_title,
                guid=item.guid,
            )
            episode.save()

def fetch_realpython_episodes():
    """Fetches new episodes from RSS for The Real Python Podcast."""
    _feed = feedparser.parse("https://realpython.com/podcasts/rpp/feed")
    save_new_episodes(_feed)

def fetch_nt_news_episodes():
    """Fetches new episodes from RSS for the Talk Python to Me Podcast."""
    _feed = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/World.xml")
    save_new_episodes(_feed)

def delete_old_job_executions(max_age=604_800):
    """Deletes all apscheduler job execution logs older than `max_age`."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)

class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            fetch_realpython_episodes,
            trigger="interval",
            minutes=1,
            id="The Real Python Podcast",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: The Real Python Podcast.")

        scheduler.add_job(
            fetch_nt_news_episodes,
            trigger="interval",
            minutes=1,
            id="NT news feed World",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: NT news feed World.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="Delete Old Job Executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: Delete Old Job Executions.")

        scheduler.add_job(
            send_email,
            # trigger=CronTrigger(day_of_week="mon-fri",hour=23),
            trigger="interval",
            minutes=1,
            id="Send email for subscribers",
            max_instances=1,
            replace_existing=True,
        )
        try:
            logger.info("Starting scheduler...")
            scheduler.start()

        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")


        # fetch_realpython_episodes()
        # fetch_talkpython_episodes()