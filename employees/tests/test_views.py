import unittest
from django.test import Client


class EmployeesTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page_view(self):
        response = self.client.get("/employees")
        self.assertEqual(response.status_code, 404)
