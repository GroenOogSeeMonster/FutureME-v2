from flask import Flask
from flask_login import LoginManager
from apscheduler.schedulers.background import BackgroundScheduler
import os
from config import Config
from app.database import db

# Initialize extensions
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    print(app.config)
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from app.user.routes import bp as user_blueprint
    app.register_blueprint(user_blueprint)

    from app.assessment import assessment as assessment_blueprint
    app.register_blueprint(assessment_blueprint)

    # Schedule job for sending emails
    if not app.debug:
        scheduler = BackgroundScheduler()
        scheduler.add_job(func=send_schedule_email, trigger="cron", day_of_week='sun', hour=18)
        scheduler.start()

    return app

from celery import Celery

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

# Create Flask app
flask_app = create_app()

# Create Celery app
celery = make_celery(flask_app)

# Import email function for sending scheduled emails
from app.main.email import send_schedule_email

# Import assessment function
from app.assessment import assessment