class UncompletedTask(db.Model):
    __tablename__ = 'uncompleted_tasks'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    task = db.Column(db.String(120), nullable=False)
    user = db.relationship('User', backref='uncompleted_tasks', lazy='dynamic')