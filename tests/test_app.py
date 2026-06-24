import pytest
from app import create_app, db
from app.models import Event, Speaker, Registration

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_dashboard_loads(client):
    # check the homepage loads correctly
    response = client.get('/')
    assert response.status_code == 200

def test_create_event(client):
    # post a new event and check it redirects (302 = success and redirect)
    response = client.post('/events/new', data={
        'name': 'Test Conference',
        'date': '2026-09-01',
        'venue': 'Test Venue',
        'description': 'A test event',
        'capacity': 100,
        'ticket_price': 25.00
    })
    assert response.status_code == 302

def test_events_page_loads(client):
    # check the events list page loads
    response = client.get('/events')
    assert response.status_code == 200
