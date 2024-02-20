from django.test import TestCase
from django.urls import reverse


class TripURLsTest(TestCase):
    def test_trip_home_url_is_correct(self):
        url = reverse('trip:criar_categoria')
        self.assertEqual(url, '/trip/criar_categoria/')
