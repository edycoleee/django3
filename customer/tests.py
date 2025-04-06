# customer/tests.py
from django.test import TestCase
from django.urls import reverse
import json

class CustomerAPITestCase(TestCase):
    
    def test_test1_customer(self):
        """Test GET /test1 returns Hello Django"""
        #Mengambil URL berdasarkan nama route (rev_test1_customer) yang sudah didefinisikan di urls.py.
        url = reverse('rev_test1_customer')
        #Simulasi request GET ke URL tersebut.
        response = self.client.get(url)
        #Memastikan response memiliki status HTTP 200 (OK).
        self.assertEqual(response.status_code, 200)
        #Key "response" ada dalam JSON.
        response_data = response.json()
        self.assertIn('response', response_data)
        #Value dari "response" adalah string "Hello Django".
        self.assertEqual(response_data["response"], "Hello Django")

    def test_test2_customer(self):
        """Test POST /test2 returns the same data"""
        url = reverse('rev_test2_customer')
        data = {"key1": "Value1", "key2": "Value2"}
        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        
        response_data = response.json()
        self.assertIn('response', response_data)
        self.assertEqual(response_data["response"], data)
