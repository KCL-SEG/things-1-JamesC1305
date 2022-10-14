from django.test import TestCase
from .models import Thing

# Create your tests here.
class ThingModelTestCase(TestCase):

    def setUp(self):
        self.thing = Thing.objects.create(
            name = "Apple",
            description = "Red and Shiny",
            quantity = 32
        )
