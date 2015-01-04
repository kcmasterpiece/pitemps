from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(StaticLiveServerTestCase):

	def setUp(self):
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
		self.assertRegex(header_text,'$Current Room Temperature: \d+°^')