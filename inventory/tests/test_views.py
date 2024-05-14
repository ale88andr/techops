import unittest
from django.test import Client


class EquipmentsTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page_view(self):
        response = self.client.get("/equipments")
        self.assertEqual(response.status_code, 404)
