import os

from flask import Flask

from .repositories.database import db
from .routes.api import api as api_blueprint


def create_app():
    app = Flask(__name__)
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"postgresql://{user}:{password}@{host}/{db_name}"
    db.init_app(app)

    # Register the API blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
