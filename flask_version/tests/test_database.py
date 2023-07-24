import unittest

from app.repositories.database import close_conn_pool, create_conn_pool
# from tests.setup_tests import *


class TestDB(unittest.TestCase):
    def test_create_and_close_conn_pool(self):
        # create pool
        pool = create_conn_pool(1, 2)

        # check that the pool is open
        self.assertFalse(pool.closed)

        # then close the connection pool
        close_conn_pool(pool)

        # check that the pool is closed
        self.assertTrue(pool.closed)
