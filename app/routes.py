from flask import Blueprint, render_template, request, redirect, url_for, flash # I imported all so its easier to use them in the routes (e.g. flask.render_template() becomes just render_template())
from app import db # All files use DB object from init.py so we can talk to the database
from app.models import Event, Speaker, Session, Registration # Importing the models so we can use them to query the database

# Create the main blueprint - groups all routes together
main = Blueprint('main', __name__)

# ─── Dashboard ───────────────────────────────────────────────────────────────

@main.route('/') # / means homepage URL. The @ decorator tells Flask that this function should be called when the user visits the homepage
def dashboard(): # fx ran when user visits homepage
    # Grab summary data for the dashboard cards. Count goes into each table and count all rows
    total_events = Event.query.count()
    total_registrations = Registration.query.count()
    total_speakers = Speaker.query.count()
    upcoming_events = Event.query.filter_by(status='upcoming').all() # Finds all events with status 'upcoming' and returns them as a list
    return render_template('dashboard.html', # Flask fx grabs html file in quotes + sends to browser (inc data)
                           total_events=total_events, # Name for html > Value from python for all these variables
                           total_registrations=total_registrations,
                           total_speakers=total_speakers,
                           upcoming_events=upcoming_events)
# Load the dashboard.html file and pass all those numbers/lists to it so the HTML can display them.

# ─── Events ──────────────────────────────────────────────────────────────────

@main.route('/events') # When someone visits /events, this function is called
def events():
    all_events = Event.query.all() # Gets the list of all events from the database and stores it in a variable not just rows count. This is a list of Event objects, not just a number
    return render_template('events/index.html', events=all_events)  
    # Like the others the html file will contain the data then the template will loop through the list and display each event in a table. 
    # The variable name 'events' is what the html file will use to access the data.