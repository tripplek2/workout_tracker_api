# Import Flask utilities
from flask import Flask, jsonify, request
from flask_migrate import Migrate

# Import database and models
from server.models import *

# Create Flask app
app = Flask(__name__)

# Configure database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Connect database
db.init_app(app)

# Enable migrations
migrate = Migrate(app, db)

#Workout routes
# Get all workouts
@app.get("/workouts")
def get_workouts():
    return jsonify({"message": "GET all workouts"}), 200


# Get one workout
@app.get("/workouts/<int:id>")
def get_workout(id):
    return jsonify({"message": f"GET workout {id}"}), 200


# Create workout
@app.post("/workouts")
def create_workout():
    return jsonify({"message": "POST workout"}), 201


# Delete workout
@app.delete("/workouts/<int:id>")
def delete_workout(id):
    return jsonify({"message": f"DELETE workout {id}"}), 200

# Exercise routes
# Get all exercises
@app.get("/exercises")
def get_exercises():
    return jsonify({"message": "GET all exercises"}), 200


# Get one exercise
@app.get("/exercises/<int:id>")
def get_exercise(id):
    return jsonify({"message": f"GET exercise {id}"}), 200


# Create exercise
@app.post("/exercises")
def create_exercise():
    return jsonify({"message": "POST exercise"}), 201


# Delete exercise
@app.delete("/exercises/<int:id>")
def delete_exercise(id):
    return jsonify({"message": f"DELETE exercise {id}"}), 200

# WorkoutExercise route
# Add exercise to workout
@app.post("/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises")
def add_exercise_to_workout(workout_id, exercise_id):
    return jsonify({
        "message": f"Add exercise {exercise_id} to workout {workout_id}"
    }), 201


if __name__ == "__main__":
    app.run(port=5555, debug=True)