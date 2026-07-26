#!/usr/bin/env python3

# Import app and models
from app import app
from models import *

with app.app_context():

    # Seed data will go here

    print("Database seeded!")