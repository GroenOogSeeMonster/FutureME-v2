from app import db
from app.models import Goal

class JournalEntry(db.Model):
    __tablename__ = 'journal_entries'
    id = db.Column(db.Integer, primary_key=True)
    goal_id = db.Column(db.Integer, db.ForeignKey('goals.id'))
    description = db.Column(db.Text, nullable=False)
    goal = db.relationship('Goal', back_populates='journal_entries')

# And in your Goal model, you should have:

class Goal(db.Model):
    # ... other fields here ...
    journal_entries = db.relationship('JournalEntry', back_populates='goal')