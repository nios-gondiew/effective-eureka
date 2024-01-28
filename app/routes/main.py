from flask import Blueprint, jsonify

# Create a Blueprint instance for the 'main' module
main_bp = Blueprint('main', __name__)

# Define routes and their handlers

@main_bp.route('/')
def index():
    return jsonify(message="Welcome to the API!")

@main_bp.route('/hello/<string:name>')
def hello(name):
    return jsonify(message=f"Hello, {name}!")

# Add more routes and handlers as needed
