# Workout Tracker API

## Overview

Workout Tracker API is a RESTful Flask application that allows users to manage workouts and exercises. The API supports creating, retrieving, updating, and deleting workouts and exercises, as well as assigning exercises to workouts with details such as sets, reps, and duration.

This project demonstrates the use of Flask, SQLAlchemy ORM, Flask-Migrate, Marshmallow, SQLite, and RESTful API design.

---

## Features

* Create, view, and delete workouts
* Create, view, and delete exercises
* Associate exercises with workouts
* Record workout details such as:

  * Sets
  * Repetitions
  * Duration
* Input validation using Marshmallow
* Database migrations using Flask-Migrate
* Seed database with sample data
* RESTful API endpoints tested using Postman

---

## Technologies Used

* Python 3.12
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* SQLAlchemy
* Marshmallow
* SQLite
* Postman
* Git & GitHub

---

## Project Structure

```text
workout_tracker_api/
│
├── migrations/
├── server/
│   ├── __init__.py
│   ├── app.py
│   ├── models.py
│   ├── schemas.py
│   └── seed.py
│
├── app.db
├── requirements.txt
├── Pipfile
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/tripplek2/workout_tracker_api.git
```

Navigate into the project:

```bash
cd workout_tracker_api
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows (Git Bash)

```bash
source venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Database Setup

Set the Flask application:

```bash
export FLASK_APP=server.app
```

Run database migrations:

```bash
flask db upgrade
```

Seed the database:

```bash
python3 -m server.seed
```

---

## Running the Application

Start the Flask server:

```bash
python3 -m server.app
```

The application will run at:

```
http://127.0.0.1:5555
```

---

## API Endpoints

### Home

| Method | Endpoint |
| ------ | -------- |
| GET    | `/`      |

---

### Workouts

| Method | Endpoint         | Description      |
| ------ | ---------------- | ---------------- |
| GET    | `/workouts`      | Get all workouts |
| GET    | `/workouts/<id>` | Get one workout  |
| POST   | `/workouts`      | Create a workout |
| DELETE | `/workouts/<id>` | Delete a workout |

---

### Exercises

| Method | Endpoint          | Description        |
| ------ | ----------------- | ------------------ |
| GET    | `/exercises`      | Get all exercises  |
| GET    | `/exercises/<id>` | Get one exercise   |
| POST   | `/exercises`      | Create an exercise |
| DELETE | `/exercises/<id>` | Delete an exercise |

---

### Workout Exercises

Associate an exercise with a workout.

| Method | Endpoint                                                           |
| ------ | ------------------------------------------------------------------ |
| POST   | `/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` |

Example request body:

```json
{
  "sets": 3,
  "reps": 12,
  "duration_seconds": 60
}
```

---

## Example JSON

### Create Exercise

```json
{
  "name": "Burpees",
  "category": "Cardio",
  "equipment_needed": false
}
```

### Create Workout

```json
{
  "date": "2026-07-27",
  "duration_minutes": 45,
  "notes": "Full body workout"
}
```

---

## Validation

The API validates user input before saving data.

Examples include:

* Exercise name must contain at least 3 characters.
* Workout duration must be greater than zero.
* Sets, reps, and duration cannot be negative.

---


## Future Improvements

* Update (PUT/PATCH) endpoints
* User authentication
* JWT authorization
* Workout statistics
* Exercise search and filtering
* Pagination

---

## Author

**Kelvin Korir**

GitHub: https://github.com/tripplek2

---

## License

This project is for educational purposes.
