from app import create_app
from flask_testing import TestCase
from tests.setup_tests import *


class TestRoutes(TestCase):
    def create_app(self):
        app = create_app()
        app.config["TESTING"] = True
        return app

    def test_api_root_route(self):
        response = self.client.get("/api")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"api root")
