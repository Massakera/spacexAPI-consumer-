from django.test import TestCase, Client
from django.urls import reverse
from main.utils import get_max_dict

class test_launch_sites(TestCase):
    @classmethod
    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("launch_sites")

    def test_launch_sites_response(self):
        request = self.client.get(self.url)
        self.assertEqual(200,request.status_code)

    def test_get_max_dict(self):
        data = [{'id':1}, {'id':1}, {'id':1}, {'id':2}, {'id':3}]
        self.assertEqual(get_max_dict(data,'id'),{'id':1})
