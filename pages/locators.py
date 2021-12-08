from selenium.webdriver.common.by import By

class ProductPageLocators():
	SUCCESS_MESSAGE=(By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner")
	LOGIN_LINK=(By.CSS_SELECTOR, "#login_link")
	BUTTON_ADD_TO_BASKET_LINK=(By.CSS_SELECTOR, ".btn-add-to-basket")
	FIELD_ALERT_INNER=(By.CSS_SELECTOR, ".alertinner")
	PRODUCT_PRICE_TEXT=(By.CSS_SELECTOR, ".product_main .price_color")
	BASKET_MINI_TEXT=(By.CSS_SELECTOR, ".basket-mini")
	BOOK_NAME_TEXT=(By.CSS_SELECTOR, ".product_main h1")

class BasePageLocators():
	LOGIN_LINK=(By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID=(By.CSS_SELECTOR, "#login_link_inc")
	LOGIN_FORM=(By.CSS_SELECTOR, ".login_form")
	REGISTER_FORM=(By.CSS_SELECTOR, ".register_form")
	BASKET_MINI_BUTTON=(By.CSS_SELECTOR, ".basket-mini .btn-default")
	BASKET_CONTENT_INNER=(By.CSS_SELECTOR, "#content_inner p")
	BASKET_CONTENT=(By.CSS_SELECTOR, ".basket-items")
	REGISTRATION_EMAIL=(By.CSS_SELECTOR, "#id_registration-email")
	REGISTRATION_PASSWORD1=(By.CSS_SELECTOR, "#id_registration-password1")
	REGISTRATION_PASSWORD2=(By.CSS_SELECTOR, "#id_registration-password2")
	REGISTRATION_BUTTON=(By.CSS_SELECTOR, "#register_form .btn-primary")
	USER_ICON=(By.CSS_SELECTOR, ".icon-user")