from django.urls import resolve, reverse
from trip import views
from django.test import TestCase


class TripTemplatesTest(TestCase):
    def test_categoria_loads_correct_template(self):
        response = self.client.get(reverse('trip:categoria'))
        self.assertTemplateUsed(response, 'trip/criar_categoria.html')
