from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the database object - shared across the whole app
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Secret key for sessions and security
    app.config['SECRET_KEY'] = 'eventmaster-secret-key'

    # Tell Flask where the SQLite database file is
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eventmaster.db'

    # Connect the database to the app
    db.init_app(app)

    # Register routes
    from app.routes import main
    app.register_blueprint(main)

    # Create database tables if they don't exist
    with app.app_context():
        from app import models
        db.create_all()

    return app
