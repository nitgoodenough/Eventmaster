from app import db

# Event table - stores all conference events
class Event(db.Model): # Model is a class that represents a table in the database
    id = db.Column(db.Integer, primary_key=True) # Primary key is a unique identifier for each row in the table
    name = db.Column(db.String(100), nullable=False) # Nullable false means this field is required
    date = db.Column(db.String(20), nullable=False)
    venue = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    capacity = db.Column(db.Integer, nullable=False, default=100) # Default values if not provided
    ticket_price = db.Column(db.Float, nullable=False, default=0.0)
    status = db.Column(db.String(20), default='upcoming')

    # One event has many sessions and registrations
    sessions = db.relationship('Session', backref='event', lazy=True)
    registrations = db.relationship('Registration', backref='event', lazy=True)

# Speaker table - stores speaker profiles
class Speaker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    email = db.Column(db.String(120), nullable=False)
    company = db.Column(db.String(100), nullable=True)

    # One speaker can have many sessions
    sessions = db.relationship('Session', backref='speaker', lazy=True)

# Session table - individual talks within a conference
class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # in minutes
    room = db.Column(db.String(50), nullable=True)

    # Links to event and speaker
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    speaker_id = db.Column(db.Integer, db.ForeignKey('speaker.id'), nullable=True)

# Registration table - stores attendee registrations
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attendee_name = db.Column(db.String(100), nullable=False)
    attendee_email = db.Column(db.String(120), nullable=False)
    ticket_type = db.Column(db.String(50), default='Standard')  # Early Bird, Standard, VIP
    payment_status = db.Column(db.String(20), default='pending')

    # Links to event
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
