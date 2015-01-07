
from django.core.urlresolvers import resolve
# from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from tempGraph.views import home_page
from tempGraph.models import Readings
from datetime import datetime
# Create your tests here.

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')

class DataModelTest(TestCase):
	
	def test_can_save_and_retrieve_readings(self):
		reading = Readings.objects.create(temp=21)
		saved_readings = Readings.objects.all()
		self.assertEqual(saved_readings[0].temp,reading.temp)

	def test_displays_current_temperature(self):
		newReadingOne =  Readings.objects.create(temp=1)
		newReadingTwo =  Readings.objects.create(temp=2)
		newReadingThree =  Readings.objects.create(temp=3)
		correctTemperature = newReadingThree.temp

		response = self.client.get('/')
		self.assertContains(response, correctTemperature)