from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    from app.user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    from app.assessment import assessment as assessment_blueprint
    app.register_blueprint(assessment_blueprint)

    return app