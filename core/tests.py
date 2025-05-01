from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client

class HolaMundo(TestCase):
    def test_hola_mundo_view(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hola Mundo')