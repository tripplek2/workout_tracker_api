#!/usr/bin/env python3

# Import app and models
from datetime import date
from server.app import app
from server.models import db, Exercise, Workout, WorkoutExercise

with app.app_context():

    # Clear existing data
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    db.session.commit()

    print("Old data deleted.")

    # Create exercises
    push_up = Exercise(
        name="Push Up",
        category="Strength",
        equipment_needed=False
    )

    squat = Exercise(
        name="Squat",
        category="Strength",
        equipment_needed=False
    )

    plank = Exercise(
        name="Plank",
        category="Core",
        equipment_needed=False
    )

    treadmill = Exercise(
        name="Treadmill Run",
        category="Cardio",
        equipment_needed=True
    )

    # Add exercises
    db.session.add_all([
        push_up,
        squat,
        plank,
        treadmill
    ])

    db.session.commit()

    print("Exercises added.")

    # Create workouts
    workout1 = Workout(
        date=date(2026, 7, 26),
        duration_minutes=45,
        notes="Upper body workout."
    )

    workout2 = Workout(
        date=date(2026, 7, 27),
        duration_minutes=60,
        notes="Leg day."
    )

    # Add workouts
    db.session.add_all([
        workout1,
        workout2
    ])

    db.session.commit()

    print("Workouts added.")

    # Link exercises to workouts
    workout_exercises = [

        WorkoutExercise(
            workout=workout1,
            exercise=push_up,
            reps=15,
            sets=3
        ),

        WorkoutExercise(
            workout=workout1,
            exercise=plank,
            duration_seconds=60,
            sets=3
        ),

        WorkoutExercise(
            workout=workout2,
            exercise=squat,
            reps=12,
            sets=4
        ),

        WorkoutExercise(
            workout=workout2,
            exercise=treadmill,
            duration_seconds=900
        )

    ]

    db.session.add_all(workout_exercises)
    db.session.commit()

    print("Workout exercises added.")
    print("Database seeded successfully!")