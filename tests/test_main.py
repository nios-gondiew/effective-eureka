import unittest
from flask import current_app
from app import create_app, db

class MainBlueprintTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_main_route(self):
        response = self.client().get('/api/v1/main')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the main route', response.data)

    def test_another_route(self):
        response = self.client().get('/api/v1/another')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This is another route', response.data)

    def test_invalid_route(self):
        response = self.client().get('/api/v1/nonexistent')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Route not found', response.data)

if __name__ == '__main__':
    unittest.main()
