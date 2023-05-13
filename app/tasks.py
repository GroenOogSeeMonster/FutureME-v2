from app import celery, db
from app.email import send_email
from app.models import User, Schedule

@celery.task
def weekly_email():
    users = User.query.all()
    for user in users:
        schedules = Schedule.query.filter_by(user_id=user.id).order_by(Schedule.day, Schedule.hour).all()
        send_email(user.email, 'Your Weekly Schedule', 'email/weekly_schedule', user=user, schedules=schedules)