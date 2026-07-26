# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Import model validator
from sqlalchemy.orm import validates

# Create database instance
db = SQLAlchemy()


# Exercise model
class Exercise(db.Model):
    __tablename__ = "exercises"

    # Primary key
    id = db.Column(db.Integer, primary_key=True)

    # Exercise name
    name = db.Column(db.String, nullable=False)

    # Exercise category
    category = db.Column(db.String, nullable=False)

    # Equipment required
    equipment_needed = db.Column(db.Boolean, nullable=False)


# Workout model
class Workout(db.Model):
    __tablename__ = "workouts"

    # Primary key
    id = db.Column(db.Integer, primary_key=True)

    # Workout date
    date = db.Column(db.Date, nullable=False)

    # Workout duration
    duration_minutes = db.Column(db.Integer, nullable=False)

    # Workout notes
    notes = db.Column(db.Text)


# Join table
class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    # Primary key
    id = db.Column(db.Integer, primary_key=True)

    # Workout foreign key
    workout_id = db.Column(
        db.Integer,
        db.ForeignKey("workouts.id"),
        nullable=False
    )

    # Exercise foreign key
    exercise_id = db.Column(
        db.Integer,
        db.ForeignKey("exercises.id"),
        nullable=False
    )

    # Number of reps
    reps = db.Column(db.Integer)

    # Number of sets
    sets = db.Column(db.Integer)

    # Duration in seconds
    duration_seconds = db.Column(db.Integer)