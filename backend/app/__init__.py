from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize extensions
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize plugins
    db.init_app(app)

    # Register Routes
    from app.routes import bp
    app.register_blueprint(bp)

    # Create Database Tables automatically (if they don't exist)
    with app.app_context():
        db.create_all()

    return app