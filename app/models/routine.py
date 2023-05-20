from app import db
from app.user.models import User

class Routine(db.Model):
    __tablename__ = 'routines'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    day_of_week = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    activity = db.Column(db.String(120), nullable=False)
    user = db.relationship('User', backref='routines')