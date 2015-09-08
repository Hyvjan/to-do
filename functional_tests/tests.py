from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(LiveServerTestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()
		
	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])
		
	def test_can_start_a_list_and_retrieve_it_later(self):
		#Edith has heard about cool online to-do app. She checks out the webpage
		self.browser.get(self.live_server_url)
		
		#She notices the webpage title and header mention to-do list
		self.assertIn('To-Do', self.browser.title)
		header_text=self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		#She is invited to enter a To-Do item straight away
		inputbox= self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		#She types "buy peacock feathers" into a text box
		inputbox.send_keys('Buy peacock feathers')

		#When she hits enter, page updates, and page lists:
		#1: Buy peacock feathers
		inputbox.send_keys(Keys.ENTER)
		self.check_for_row_in_list_table('1: Buy peacock feathers')

		#There is still a text box inviting her to add another item
		#She enters "use peacock feathers to make a fly
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

	#Page updates again and shows both items on her list
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

	#Edith wonders weather page remembers her list. Site has genereated a unique URL for her
		self.fail('Finish the test!')

	#She visits that URL- her to-do list is still there

	#She goes back to sleep

if __name__=='__main__':
	unittest.main(warnings='ignore')

