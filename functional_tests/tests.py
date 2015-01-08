from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tempGraph.models import Readings
from datetime import datetime
import sys
import unittest

class NewVisitorTest(StaticLiveServerTestCase):

	@classmethod
	def setUpClass(cls):
		for arg in sys.argv:
			if 'liveserver' in arg:
				cls.server_url = 'http://' + arg.split('=')[1]
				return
		super().setUpClass()
		cls.server_url = cls.live_server_url

	@classmethod
	def tearDownClass(cls):
		if cls.server_url == cls.server_url:
			super().tearDownClass()

	def setUp(self):
		newReading = Readings.objects.create(temp=99)
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_open_website(self):

		# Open the website
		self.browser.get(self.server_url)

		# Observe page title and header elements
		self.assertIn('Current Room Temps', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertRegex(header_text,r"^Current Room Temperature: \d+°$")

		
	def test_layout_and_styling(self):
		# Open home page
		self.browser.get(self.server_url)
		self.browser.set_window_size(1024,768)
		# check centered header
		header = self.browser.find_element_by_tag_name('h1')
		header_text_alignment = header.value_of_css_property("text-align")
		self.assertEqual(header_text_alignment, 'center')

