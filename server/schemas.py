# Import Marshmallow
from marshmallow import Schema, fields

# Exercise Schema
class ExerciseSchema(Schema):
    # Exercise ID
    id = fields.Int(dump_only=True)

    # Exercise name
    name = fields.Str(required=True)

    # Exercise category
    category = fields.Str(required=True)

    # Equipment required
    equipment_needed = fields.Bool(required=True)

    # WorkoutExercise Schema
class WorkoutExerciseSchema(Schema):
    #Join table ID 
    id = fields.Int(dump_only=True)

    # Foreign keys
    workout_id = fields.Int()
    exercise_id = fields.Int()

    # Workout details
    reps = fields.Int(allow_none=True)
    sets = fields.Int(allow_none=True)
    duration_seconds = fields.Int(allow_none=True)

    # Workout Schema
class WorkoutSchema(Schema):
    # Workout ID
    id = fields.Int(dump_only=True)

    # Workout information
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str()

    # Related exercises
    exercises = fields.Nested(
        ExerciseSchema,
        many=True,
        dump_only=True
    )

# Exercise schemas
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

# Workout schemas
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

# WorkoutExercise schemas
workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)