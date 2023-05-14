from app import db

class GoalCategory(db.Model):
    __tablename__ = 'goal_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    goals = db.relationship('Goal', backref='category', lazy='dynamic')

class Goal(db.Model):
    __tablename__ = 'goals'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('goal_categories.id'))
    text = db.Column(db.String(250), nullable=False)
    notes = db.Column(db.Text, nullable=True)