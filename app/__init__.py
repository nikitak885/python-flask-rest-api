from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # Initialize the database
    db.init_app(app)

    # Register blueprints (views)
    from .views.user_view import user_blueprint
    app.register_blueprint(user_blueprint)

    return app
