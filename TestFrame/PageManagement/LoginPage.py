from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage(BasePage):
	"""docstring for LoginPage"""
	username = (By.ID, 'username id in page')
	password = (By.ID, 'password id in page')
	submit_button = (By.ID, 'submit button id in page')

	def set_username(self, username):	
		name = self.driver.find_element(*LoginPage.username)
		name.sendkeys(username)

	def set_password(self,password):
		pwd = self.driver.find_element(*LoginPage.password)
		pwd.sendkeys(password)

	def click_Signin(self):
		signin_btn = self.driver.find_element(*LoginPage.submit_button)