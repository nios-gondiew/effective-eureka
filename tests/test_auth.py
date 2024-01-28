import json
import unittest
from app import create_app, db

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.app = create_app('testing')
        self.client = self.app.test_client

        # Initialize the test database
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """Tear down the test environment."""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_registration(self):
        """Test user registration."""
        response = self.client().post('/api/register', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')

        data = json.loads(response.data.decode())
        self.assertTrue(response.status_code, 201)
        self.assertIn('Successfully registered', data['message'])

    def test_login(self):
        """Test user login."""
        # First, register a test user
        self.client().post('/api/register', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')

        # Then, attempt to log in with the registered user credentials
        response = self.client().post('/api/login', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')

        data = json.loads(response.data.decode())
        self.assertTrue(response.status_code, 200)
        self.assertIn('Successfully logged in', data['message'])
        self.assertIn('access_token', data)

    def test_login_invalid_credentials(self):
        """Test login with invalid credentials."""
        response = self.client().post('/api/login', data=json.dumps({
            'username': 'invaliduser',
            'password': 'invalidpassword'
        }), content_type='application/json')

        data = json.loads(response.data.decode())
        self.assertTrue(response.status_code, 401)
        self.assertIn('Invalid credentials', data['message'])

if __name__ == '__main__':
    unittest.main()
