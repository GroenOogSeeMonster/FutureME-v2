from flask import render_template
from flask_mail import Message
from app.user.models import User
from app.models.routine import Routine

def send_schedule_email(app):
    with app.app_context():
        users = User.query.all()
        for user in users:
            goals = user.goals.all()
            routines = user.routines.order_by(Routine.day_of_week, Routine.start_time).all()
            msg = Message('Your weekly schedule and goals', recipients=[user.email])
            msg.body = render_template('email/schedule.txt', user=user, goals=goals, routines=routines)
            app.mail.send(msg)
