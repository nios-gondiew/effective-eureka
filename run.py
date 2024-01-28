from flask import Flask
from .config import app_config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    # Additional configurations or extensions can be added here

    # Import and register blueprints
    from .routes.auth import auth_blueprint
    from .routes.main import main_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(main_blueprint, url_prefix='/api')

    return app
