from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager
from app.database import db
from datetime import datetime

class Assessment1Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    answer1 = db.Column(db.String(1000))
    answer2 = db.Column(db.String(1000))
    answer3 = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(120), unique=True)
    cell_number = db.Column(db.String(15))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))