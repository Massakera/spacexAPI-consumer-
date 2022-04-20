from django.test import TestCase, Client
from django.urls import reverse
from main.utils import most_frequent

class test_launches(TestCase):
    @classmethod
    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("launches")

    def test_launches_response(self):
        request = self.client.get(self.url)
        self.assertEqual(200,request.status_code)

    def test_most_frequent_not_null(self):
        test_list = ['a','3','a']
        self.assertEqual(most_frequent(test_list),'a')

