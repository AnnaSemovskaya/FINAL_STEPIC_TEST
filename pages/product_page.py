from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
	def btn_add_to_basket_find(self):
		assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET_LINK), "Add to basket button is not presented"

	def btn_add_to_basket_click(self):
		button=self.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET_LINK)
		button.click()

	def should_be_alert_inners(self):
		assert self.are_elements_present(*ProductPageLocators.FIELD_ALERT_INNER), "Alerts are not presented"

	def check_price_from_alerts(self):
		price=self.find_element(*ProductPageLocators.PRODUCT_PRICE_TEXT).text
		basket=self.find_element(*ProductPageLocators.BASKET_MINI_TEXT).text
		assert basket.find(price)!=-1, "Price is different"

	def check_book(self):
		bookname=self.find_element(*ProductPageLocators.BOOK_NAME_TEXT).text
		alert_message=self.find_elements(*ProductPageLocators.FIELD_ALERT_INNER)[0].text
		assert alert_message==bookname + " has been added to your basket.", "Bookname is different"

	def check_success_message_presence(self):
		assert self.is_not_element_present(By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner")
		
	def check_success_message_disappeared(self):
		assert self.is_disappeared(By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner")

