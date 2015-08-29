from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()
		
	def test_can_start_a_list_and_retrieve_it_later(self):
		#Edith has heard about cool online to-do app. She checks out the webpage
		self.browser.get('http://localhost:8000')
		
		#She notices the webpage title and header mention to-do list
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the Test!')
		
		#She is invited to enter a To-Do item straight away

		#She types "buy peacock feathers" into a text box

		#When she hits enter, page updates, and page lists:
		#1: Buy peacock feathers

		#There is still a text box inviting her to add another item
		#She enters "use peacock feathers to make a fly

	#Page updates again and shows both items on her list

	#Edith wonders weather page remembers her list. Site has genereated a unique URL for her

	#She visits that URL- her to-do list is still there

	#She goes back to sleep

if __name__=='__main__':
	unittest.main(warnings='ignore')

