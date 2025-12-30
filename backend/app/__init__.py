from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

# Initialize extensions
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    # Enable CORS - allow requests from any origin
    # This allows your Frontend to talk to Backend from different ports/IPs
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Initialize plugins
    db.init_app(app)

    # Register Routes
    from app.routes import bp
    app.register_blueprint(bp)

    # Create Database Tables automatically (if they don't exist)
    with app.app_context():
        db.create_all()

    return app
