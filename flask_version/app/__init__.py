from app.repositories.database import close_conn_pool, create_conn_pool
from app.routes.api import api as api_blueprint
from flask import Flask, g


def create_app():
    app = Flask(__name__)

    # Create a connection pool
    app.config["DB_CONN_POOL"] = create_conn_pool(1, 5)

    @app.before_request
    def before_request():
        g.db_conn = app.config["DB_CONN_POOL"].getconn()

    @app.teardown_request
    def teardown_request(exception=None):
        db_conn = g.pop("db_conn", None)
        if db_conn:
            db_conn.close()
            app.config["DB_CONN_POOL"].putconn(db_conn)

    # Register the API blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
