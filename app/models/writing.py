from app import db
from app.models import User

class Prompt(db.Model):
    __tablename__ = 'prompts'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(2000), nullable=False)
    responses = db.relationship('WritingResponse', backref='prompt', lazy='dynamic')

class WritingResponse(db.Model):
    __tablename__ = 'writing_responses'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    prompt_id = db.Column(db.Integer, db.ForeignKey('prompts.id'))
    answer = db.Column(db.Text, nullable=False)