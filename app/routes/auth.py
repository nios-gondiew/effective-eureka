# app/routes/auth.py

from flask import Blueprint, request, jsonify
from app.services.user_service import authenticate_user, create_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Missing username or password'}), 400

    username = data['username']
    password = data['password']

    if create_user(username, password):
        return jsonify({'message': 'User created successfully'}), 201
    else:
        return jsonify({'error': 'User with this username already exists'}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Missing username or password'}), 400

    username = data['username']
    password = data['password']

    user = authenticate_user(username, password)

    if user:
        # In a real application, you would generate a JWT token here for authentication.
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401
