from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tempGraph.models import Readings
from datetime import datetime
import re
import unittest

class NewVisitorTest(StaticLiveServerTestCase):

	def setUp(self):
		newReading = Readings.objects.create(temp=99)
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_open_website(self):

		# Open the website
		self.browser.get(self.live_server_url)

		# Observe page title and header elements
		self.assertIn('Current Room Temps', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertRegex(header_text,r"^Current Room Temperature: \d+°$")

		
	def test_layout_and_styling(self):
		# Open home page
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024,768)
		# check centered header
		header = self.browser.find_element_by_tag_name('h1')
		header_text_alignment = header.value_of_css_property("text-align")
		self.assertEqual(header_text_alignment, 'center')

