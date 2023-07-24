from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path(__file__).parent.parent / ".env.testing"
load_dotenv(dotenv_path.resolve())

import os

from app import create_app
from flask_testing import TestCase


class TestRoutes(TestCase):
    def create_app(self):
        app = create_app()
        app.config["TESTING"] = True
        return app

    def test_api_root_route(self):
        response = self.client.get("/api")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "api root")

    def test_get_top_n(self):
        response = self.client.get("/api/top?n=2")
        if response.status_code != 200:
            print(response.json)

        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)
        for item in data:
            self.assertIn("id", item)
            self.assertIn("url", item)
            self.assertIn("title", item)
            self.assertIn("lang", item)
            self.assertIn("html_content", item)
            self.assertIn("last_crawled", item)
            self.assertIn("last_updated", item)
            self.assertIn("last_updated_date", item)
            self.assertIn("score", item)

    def test_get_top_n_no_n(self):
        response = self.client.get("/api/top")
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)

    def test_get_top_n_less_than_1(self):
        response = self.client.get("/api/top?n=0")
        self.assertEqual(response.status_code, 400)

    def test_get_top_n_greater_than_100(self):
        response = self.client.get("/api/top?n=101")
        self.assertEqual(response.status_code, 400)

    def test_get_top_n_not_a_number(self):
        response = self.client.get("/api/top?n=abc")
        self.assertEqual(response.status_code, 200)
