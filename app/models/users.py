# app/models/user.py

from app import db  # Assuming you have a Flask SQLAlchemy instance named 'db'

class User(db.Model):
    """User model for the application."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"
