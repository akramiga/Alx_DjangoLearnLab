from django.test import TestCase
from rest_framework import status

# Create your tests here.
class ApiTests(TestCase):
    def setUp(self):
        ...
    def tearDown(self):
        ...    
    def test_book_list(self):
        response = self.client.get("/list/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
            
    def test_book_create(self):
        ...   
    def test_book_update(self):
        ...   
    def test_book_delete(self):
        ...       