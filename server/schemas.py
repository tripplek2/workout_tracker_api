# Import Marshmallow
from marshmallow import Schema, fields, validates, ValidationError

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

    # Validate exercise name
    @validates("name")
    def validate_name(self, value):
        if len(value.strip()) < 3:
            raise ValidationError(
                "Exercise name must have at least 3 characters."
            )

    # Validate category
    @validates("category")
    def validate_category(self, value):
        if not value.strip():
            raise ValidationError(
                "Category is required."
            )

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

    # Validate reps
    @validates("reps")
    def validate_reps(self, value):
        if value is not None and value < 0:
            raise ValidationError(
                "Reps cannot be negative."
            )

    # Validate sets
    @validates("sets")
    def validate_sets(self, value):
        if value is not None and value < 0:
            raise ValidationError(
                "Sets cannot be negative."
            )

    # Validate duration
    @validates("duration_seconds")
    def validate_duration(self, value):
        if value is not None and value < 0:
            raise ValidationError(
                "Duration cannot be negative."
            )

    # Validate workout duration
    @validates("duration_minutes")
    def validate_duration(self, value):
        if value <= 0:
            raise ValidationError(
                "Duration must be greater than zero."
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