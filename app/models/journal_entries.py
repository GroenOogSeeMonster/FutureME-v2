from app import db
from app.models import User, Goal

class JournalEntry(db.Model):
    __tablename__ = 'journal_entries'
    id = db.Column(db.Integer, primary_key=True)
    goal_id = db.Column(db.Integer, db.ForeignKey('goals.id'))
    description = db.Column(db.Text, nullable=False)
    goal = db.relationship('Goal', backref='journal_entries', lazy='dynamic')