import os
from celery.schedules import crontab

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
    CELERY_BEAT_SCHEDULE = {
        'weekly-email': {
            'task': 'app.tasks.weekly_email',
            'schedule': crontab(hour=18, day_of_week=6),
        },
    }