from __future__ import unicode_literals
import unittest
import todoer.todoer


class TodoerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = todoer.todoer.app.test_client()

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.data, b"Hello world")
