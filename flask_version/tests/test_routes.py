from app import create_app
from flask_testing import TestCase


class TestRoutes(TestCase):
    def create_app(self):
        app = create_app()
        app.config["TESTING"] = True
        return app

    def test_home_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, World!")
