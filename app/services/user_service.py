# app/services/user_service.py

from app.models.user import User
from app import db

def create_user(username, email, password):
    """
    Create a new user and add it to the database.
    """
    new_user = User(username=username, email=email, password=password)
    
    db.session.add(new_user)
    db.session.commit()
    
    return new_user

def get_user_by_id(user_id):
    """
    Retrieve a user by their ID.
    """
    return User.query.get(user_id)

def get_user_by_username(username):
    """
    Retrieve a user by their username.
    """
    return User.query.filter_by(username=username).first()

def authenticate_user(username, password):
    """
    Authenticate a user based on username and password.
    """
    user = get_user_by_username(username)
    
    if user and user.check_password(password):
        return user
    
    return None
