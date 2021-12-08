from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException 
from selenium.common.exceptions import TimeoutException 
import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

EMPTY_MEGGAGE="Your basket is empty."

class BasePage():
	def __init__(self, browser, url, timeout=10):
		self.browser=browser
		self.url=url
		self.browser.implicitly_wait(timeout)

	def open(self):
		self.browser.get(self.url)

	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how,what)
		except(NoSuchElementException):
			return False
		return True

	def are_elements_present(self, how, what):
		elements=self.browser.find_elements(how,what)
		return (len(elements)!=0)

	def find_element(self, how, what):
		try:
			element=self.browser.find_element(how,what)
		except(NoSuchElementException):
			return None
		return element

	def find_elements(self, how, what):
		try:
			elements=self.browser.find_elements(how,what)
		except(NoSuchElementException):
			return None 
		return elements

	def solve_quiz_and_get_code(self):
	    alert = self.browser.switch_to.alert
	    x = alert.text.split(" ")[2]
	    answer = str(math.log(abs((12 * math.sin(float(x))))))
	    alert.send_keys(answer)
	    alert.accept()
	    try:
	        alert = self.browser.switch_to.alert
	        alert_text = alert.text
	        print(f"Your code: {alert_text}")
	        alert.accept()
	    except NoAlertPresentException:
	        print("No second alert presented")

	def is_not_element_present(self, how, what, timeout=10):
	    try:
	        WebDriverWait(self.browser, timeout, 1, TimeoutException).until(EC.presence_of_element_located((how, what)))
	    except TimeoutException:
	        return True
	    return False

	def is_disappeared(self, how, what, timeout=10):
	    try:
		    print(how)
		    print(what)
		    WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
	    except TimeoutException:
	        return False
	    return True

	def go_to_login_page(self):
		login_link=self.browser.find_element(*BasePageLocators.LOGIN_LINK)
		login_link.click()

	def check_login_was_successful(self):
		assert self.is_element_present(*BasePageLocators.LOGIN_FORM), "Login form is not presented"

	def should_be_login_link(self):
		assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

	def button_basket_press(self):
		button=self.find_element(*BasePageLocators.BASKET_MINI_BUTTON)
		button.click()
		assert self.is_element_present(*BasePageLocators.BASKET_CONTENT_INNER)

	def check_basket_has_empty_message(self):
		content=self.find_element(*BasePageLocators.BASKET_CONTENT_INNER).text
		print(content)
		assert content.find(EMPTY_MEGGAGE)!=-1, "Wrong message about empty basket."

	def check_basket_is_empty(self):
		assert self.is_not_element_present(*BasePageLocators.BASKET_CONTENT)

	def should_be_authorized_user(self):
		assert self.is_element_present(*BasePageLocators.USER_ICON)

