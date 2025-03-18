from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class ApiTests(TestCase):
    def setUp(self):
        ...
    def tearDown(self):
        ...    
    def test_book_list(self):
        response = self.client.get("/books/list/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,[])  #logic to be improved
            
    def test_book_create(self):
        response = self.client.post("/books/create/")
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.assertEqual(response.data,[])  #logic to be improved 

    def test_book_update(self):
        response = self.client.put("/books/update/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)   
        self.assertEqual(response.data,[])  #logic to be improved

    def test_book_delete(self):
        response = self.client.delete("/books/delete/")
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.assertEqual(response.data,[])  #logic to be improved    