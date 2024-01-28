from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy instance
db = SQLAlchemy()

# Import your models to make them available when the application is run
from .user import User  # You should replace "user" with the actual model name

# Additional initialization or configuration code for your models can be added here
