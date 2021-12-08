from .base_page import BasePage
from .locators import BasePageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        loginurl=self.findelement(*BasePageLocators.LOGIN_LINK)
        assert loginurl.text.find("login")!=-1, "Wrong login url"

    def should_be_login_form(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*BasePageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        emailfield=self.find_element(*BasePageLocators.REGISTRATION_EMAIL)
        emailfield.send_keys(email)
        password1field=self.find_element(*BasePageLocators.REGISTRATION_PASSWORD1)
        password1field.send_keys(password)
        password2field=self.find_element(*BasePageLocators.REGISTRATION_PASSWORD2)
        password2field.send_keys(password)
        button=self.find_element(*BasePageLocators.REGISTRATION_BUTTON)
        button.click()
