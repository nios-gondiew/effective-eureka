from app import create_app

# Load the development configuration by default
# You can change this to 'production' or 'testing' as needed
config_name = 'development'

app = create_app(config_name)

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
