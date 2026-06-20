from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Event, Speaker, Session, Registration

# Create the main blueprint - groups all routes together
main = Blueprint('main', __name__)
