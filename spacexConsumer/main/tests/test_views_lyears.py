from django.test import TestCase, Client
from django.urls import reverse


class test_launch_sites(TestCase):
    @classmethod
    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("launches_2019_2021")

    def test_launches_2019_2021_response(self):
        request = self.client.get(self.url)
        self.assertEqual(200,request.status_code)