import os

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Use an appropriate database URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use an in-memory database for testing

class ProductionConfig(Config):
    # Add production-specific configurations here
    pass

# Define the configuration to be used based on the environment
config_mapping = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}

# Get the current environment from the environment variable or default to 'development'
environment = os.environ.get('FLASK_ENV', 'development')

# Select the appropriate configuration
config = config_mapping.get(environment.lower(), DevelopmentConfig)
