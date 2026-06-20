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
    return render_template('dashboard.html',
                           total_events=total_events, # Name for html > Value from python for all these variables
                           total_registrations=total_registrations,
                           total_speakers=total_speakers,
                           upcoming_events=upcoming_events)
# Load the dashboard.html file and pass all those numbers/lists to it so the HTML can display them.

# ─── Events ──────────────────────────────────────────────────────────────────

@main.route('/events')
def events():
    all_events = Event.query.all()
    return render_template('events/index.html', events=all_events)

@main.route('/events/new', methods=['GET', 'POST'])
def new_event():
    if request.method == 'POST':
        event = Event(
            name=request.form['name'],
            date=request.form['date'],
            venue=request.form['venue'],
            description=request.form.get('description', ''),
            capacity=int(request.form['capacity']),
            ticket_price=float(request.form['ticket_price'])
        )
        db.session.add(event)
        db.session.commit()
        flash('Event created successfully!', 'success')
        return redirect(url_for('main.events'))
    return render_template('events/new.html')

@main.route('/events/<int:id>')
def event_detail(id):
    event = Event.query.get_or_404(id)
    return render_template('events/detail.html', event=event)

@main.route('/events/<int:id>/edit', methods=['GET', 'POST'])
def edit_event(id):
    event = Event.query.get_or_404(id)
    if request.method == 'POST':
        event.name = request.form['name']
        event.date = request.form['date']
        event.venue = request.form['venue']
        event.description = request.form.get('description', '')
        event.capacity = int(request.form['capacity'])
        event.ticket_price = float(request.form['ticket_price'])
        db.session.commit()
        flash('Event updated!', 'success')
        return redirect(url_for('main.events'))
    return render_template('events/edit.html', event=event)

@main.route('/events/<int:id>/delete', methods=['POST'])
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    flash('Event deleted.', 'info')
    return redirect(url_for('main.events'))
