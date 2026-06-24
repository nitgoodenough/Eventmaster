# EventMaster

A web-based event management system built for BrightEvents, focused on managing Conference events. Built as part of module WM278-30 (SDLC) Assignment 3.

## Tech Stack

- **Backend:** Python + Flask
- **Database:** SQLite via Flask-SQLAlchemy
- **Frontend:** Bootstrap 5 + plain JavaScript
- **Testing:** pytest

## Features

- Create, view, edit and delete conference events
- Manage speakers and their profiles
- Register attendees for events
- Reports page showing event stats and estimated revenue

## Setup Instructions

1. Clone the repo
```
git clone https://github.com/nitgoodenough/Eventmaster.git
cd Eventmaster
```

2. Create and activate a virtual environment
```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Run the app
```
python run.py
```

5. Open your browser and go to `http://127.0.0.1:5000`

## Running Tests

```
pytest tests/test_app.py -v
```

## Project Structure

```
Eventmaster/
├── app/
│   ├── __init__.py        # app factory, database setup
│   ├── models.py          # database table definitions
│   ├── routes.py          # all URL routes
│   ├── static/
│   │   └── style.css      # custom styles
│   └── templates/
│       ├── base.html
│       ├── dashboard.html
│       ├── events/
│       ├── speakers/
│       ├── registrations/
│       └── reports/
├── tests/
│   └── test_app.py
├── run.py
└── requirements.txt
```
