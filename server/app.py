# Import Flask utilities
from flask import Flask
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

# Routes will go here


if __name__ == "__main__":
    app.run(port=5555, debug=True)