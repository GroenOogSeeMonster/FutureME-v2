from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    from app.user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    from app.assessment import assessment as assessment_blueprint
    app.register_blueprint(assessment_blueprint)

    return app

    from apscheduler.schedulers.background import BackgroundScheduler
    from app.main.email import send_schedule_email

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

celery = make_celery(flask_app)
