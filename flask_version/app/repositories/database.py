import os

from psycopg2 import pool


def create_conn_pool(minconn, maxconn):
    """Create a connectio pool."""
    try:
        print("Creating pool")
        conn_pool = pool.SimpleConnectionPool(
            minconn,
            maxconn,
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        return conn_pool
    except Exception as e:
        print(f"Error occurred when creating connection pool: {e}")
        raise


def close_conn_pool(conn_pool):
    """Close all connections in the connection pool."""
    try:
        print("Closing pool")
        if conn_pool and not conn_pool.closed:
            conn_pool.closeall()
    except Exception as e:
        print(f"An error occurred while closing the connection pool: {e}")
        raise
