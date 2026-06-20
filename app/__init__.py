from flask import Flask # Importing flask so we can use the framework to create our app
from flask_sqlalchemy import SQLAlchemy # This will talk to the SQLite database

# Create the database object - shared across the whole app (all files use this same object)
db = SQLAlchemy()

def create_app(): # Function that builds the app when run.py is ran
    app = Flask(__name__) # Creates the flask app, name tells where it lives (app)

    # Secret key for sessions and security
    app.config['SECRET_KEY'] = 'eventmaster-secret-key'

    # Tell Flask where the SQLite database file is (auto makes if non existent yet)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eventmaster.db'

    # Connect the database earlier to the app
    db.init_app(app)

    # Register routes, then add to the app so it knows where to look for them
    from app.routes import main 
    app.register_blueprint(main) # register_blueprint adds the routes

    # Create database tables if they don't exist
    with app.app_context():
        from app import models
        db.create_all() # Built in function that creates the tables in db

    return app
