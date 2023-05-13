class Schedule(db.Model):
    __tablename__ = 'schedules'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    day = db.Column(db.String(20), nullable=False)
    hour = db.Column(db.Integer, nullable=False)
    activity = db.Column(db.String(120), nullable=False)
    user = db.relationship('User', backref='schedules', lazy='dynamic')