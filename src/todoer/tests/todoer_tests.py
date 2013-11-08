import unittest
import todoer.todoer


class TodoerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = todoer.todoer.app.test_client()

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.data, "Hello world")
