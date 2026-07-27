# Import Flask utilities
from flask import Flask, request
from flask_migrate import Migrate
from marshmallow import ValidationError
from pathlib import Path

# Import database and models
from server.models import db, Exercise, Workout, WorkoutExercise

# Import schemas
from server.schemas import (
    workout_schema,
    workouts_schema,
    exercise_schema,
    exercises_schema,
    workout_exercise_schema,
)


# Create Flask app
app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "app.db"

# Configure database
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Connect database
db.init_app(app)

# Enable migrations
migrate = Migrate(app, db)

# Home route
@app.get("/")
def home():

    return {
        "message":"Workout Tracker API",
        "version":"1.0"
    },200

#Workout routes

# Get all workouts
@app.get("/workouts")
def get_workouts():

    workouts = Workout.query.all()

    return workouts_schema.dump(workouts), 200


# Get one workout
@app.get("/workouts/<int:id>")
def get_workout(id):

    workout = db.session.get(Workout,id)

    if not workout:
        return {"error": "Workout not found"}, 404

    return workout_schema.dump(workout), 200


# Create workout
@app.post("/workouts")
def create_workout():
    try:

        data = workout_schema.load(request.get_json())

        workout = Workout(**data)

        db.session.add(workout)
        db.session.commit()

        return workout_schema.dump(workout), 201

    except ValidationError as err:

        return err.messages, 400

    except Exception as err:

        return {"error": str(err)}, 400


# Delete workout
@app.delete("/workouts/<int:id>")
def delete_workout(id):
    workout = db.session.get(Workout, id)

    if not workout:
        return {"error": "Workout not found"}, 404

    db.session.delete(workout)
    db.session.commit()

    return {"message": "Workout deleted successfully"}, 200

# Exercise routes
# Get all exercises
@app.get("/exercises")
def get_exercises():
    exercises = Exercise.query.all()

    return exercises_schema.dump(exercises), 200


# Get one exercise
@app.get("/exercises/<int:id>")
def get_exercise(id):
    exercise = db.session.get(Exercise, id)

    if not exercise:
        return {"error": "Exercise not found"}, 404

    return exercise_schema.dump(exercise), 200


# Create exercise
@app.post("/exercises")
def create_exercise():
    try:

        data = exercise_schema.load(request.get_json())

        exercise = Exercise(**data)

        db.session.add(exercise)
        db.session.commit()

        return exercise_schema.dump(exercise), 201

    except ValidationError as err:

        return err.messages, 400

    except Exception as err:

        return {"error": str(err)}, 400


# Delete exercise
@app.delete("/exercises/<int:id>")
def delete_exercise(id):
    exercise = db.session.get(Exercise, id)

    if not exercise:
        return {"error": "Exercise not found"}, 404

    db.session.delete(exercise)
    db.session.commit()

    return {"message": "Exercise deleted successfully"}, 200

# WorkoutExercise route
# Add exercise to workout
@app.post("/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises")
def add_exercise_to_workout(workout_id, exercise_id):
    workout = db.session.get(Workout, workout_id)

    if workout is None:
        return {"error":"Workout not found"},404

    exercise = db.session.get(Exercise, exercise_id)

    if exercise is None:
        return {"error":"Exercise not found"},404

    try:

        data = workout_exercise_schema.load(request.get_json())

        workout_exercise = WorkoutExercise(
            workout=workout,
            exercise=exercise,
            **data
        )

        db.session.add(workout_exercise)

        db.session.commit()

        return workout_exercise_schema.dump(workout_exercise),201

    except ValidationError as err:

        return err.messages,400


if __name__ == "__main__":
    app.run(port=5555, debug=True)