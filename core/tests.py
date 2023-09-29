from django.test import TestCase,Client
from ninja import Router
from core.models import Seed
import json


class MyModelTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.mymodel = Seed.objects.create(scan_id=6, col=0, row=1, status='ok')

    def test_get_seed(self):
        response = self.client.get("/api/seeds/6")
        self.assertEqual(response.status_code, 200)


    def test_add_tag(self):
        expected_data = { 
        "type": "trysf",
        "value": "Assff",
        "deleted": False,
        "short_name": "SN"
    }
        data = json.dumps(expected_data)
        response = self.client.post("/api/tags", data=data, content_type="application/json")
        self.assertEqual(response.status_code, 200)
