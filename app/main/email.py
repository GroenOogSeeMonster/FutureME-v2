from flask import render_template
from app import mail
from flask_mail import Message
from app.models import User
from app import create_app

def send_schedule_email():
    app = create_app()
    with app.app_context():
        users = User.query.all()
        for user in users:
            goals = user.goals.all()
            routines = user.routines.order_by(Routine.day_of_week, Routine.start_time).all()
            msg = Message('Your weekly schedule and goals', recipients=[user.email])
            msg.body = render_template('email/schedule.txt', user=user, goals=goals, routines=routines)
            mail.send(msg)