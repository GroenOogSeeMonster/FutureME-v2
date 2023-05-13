import os
from celery.schedules import crontab

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@db/futureme'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    CELERY_BEAT_SCHEDULE = {
        'weekly-email': {
            'task': 'app.tasks.weekly_email',
            'schedule': crontab(hour=18, day_of_week=6),
        },
    }