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
    name = db.Column(db.String(100), nullable=False, unique=True)

    # Exercise category
    category = db.Column(db.String(50), nullable=False)

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

    @validates("name")
    def validate_name(self, key, value):
        """Ensure exercise name is valid."""

        if not value:
            raise ValueError("Exercise name is required.")

        if len(value.strip()) < 3:
            raise ValueError("Exercise name must have at least 3 characters.")

        return value.title()

    @validates("category")
    def validate_category(self, key, value):
        """Ensure category is valid."""

        if not value:
            raise ValueError("Category is required.")

        return value.title()


# Workout model
class Workout(db.Model):
    __tablename__ = "workouts"

    __table_args__ = (
    db.CheckConstraint(
        "duration_minutes > 0",
        name="check_duration_positive"
    ),
)

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

    @validates("duration_minutes")
    def validate_duration(self, key, value):
        """Ensure workout duration is positive."""

        if value <= 0:
            raise ValueError("Duration must be greater than zero.")

        return value


# Join table
class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    __table_args__ = (

    db.CheckConstraint(
        "reps >= 0",
        name="check_reps_positive"
    ),

    db.CheckConstraint(
        "sets >= 0",
        name="check_sets_positive"
    ),

    db.CheckConstraint(
        "duration_seconds >= 0",
        name="check_duration_seconds_positive"
    ),

)

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

    @validates("reps")
    def validate_reps(self, key, value):
        """Ensure reps are valid."""

        if value is not None and value < 0:
            raise ValueError("Reps cannot be negative.")

        return value

    @validates("sets")
    def validate_sets(self, key, value):
        """Ensure sets are valid."""

        if value is not None and value < 0:
            raise ValueError("Sets cannot be negative.")

        return value

    @validates("duration_seconds")
    def validate_duration_seconds(self, key, value):
        """Ensure duration is valid."""

        if value is not None and value < 0:
            raise ValueError("Duration cannot be negative.")

        return value