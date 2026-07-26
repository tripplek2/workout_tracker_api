# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Import model validator
from sqlalchemy.orm import validates, relationship
from sqlalchemy.ext.associationproxy import association_proxy

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

    # Relationship to join table
    workout_exercises = relationship(
        "WorkoutExercise",
        back_populates="exercise",
        cascade="all, delete-orphan"
    )

    # Access related workouts
    workouts = association_proxy("workout_exercises", "workout")


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

    # Relationship to join table
    workout_exercises = relationship(
        "WorkoutExercise",
        back_populates="workout",
        cascade="all, delete-orphan"
    )

    # Access related exercises
    exercises = association_proxy("workout_exercises", "exercise")


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

    # Relationship to Workout
    workout = relationship(
        "Workout",
        back_populates="workout_exercises"
    )

    # Relationship to Exercise
    exercise = relationship(
        "Exercise",
        back_populates="workout_exercises"
    )