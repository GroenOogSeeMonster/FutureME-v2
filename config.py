import os
from celery.schedules import crontab

class Config(object):
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
    CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']
    CELERY_BEAT_SCHEDULE = {
        'weekly-email': {
            'task': 'app.tasks.weekly_email',
            'schedule': crontab(hour=18, day_of_week=6),
        },
    }