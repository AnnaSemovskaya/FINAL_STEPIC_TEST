from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import time
import pytest

#PRODUCT_PAGE_LINK="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#PRODUCT_PAGE_LINK="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
PRODUCT_PAGE_PROMO_LINK="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo="
PRODUCT_PAGE_LINK="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
PRODUCT_TEST_LOGIN_LINK="http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.parametrize('link', ["offer0",
                                  "offer1",
                                  "offer2",
                                  "offer3",
                                  "offer4",
                                  "offer5",
                                  "offer6",
                                  pytest.param("offer7", marks=pytest.mark.xfail),
                                  "offer8",
                                  "offer9"])
def test_guest_can_add_product_to_basket_promo(browser, link):
    page=ProductPage(browser, PRODUCT_PAGE_PROMO_LINK + link)
    page.open()
    page.btn_add_to_basket_find()
    page.btn_add_to_basket_click()
    page.solve_quiz_and_get_code()
    page.should_be_alert_inners()
    page.check_price_from_alerts()
    page.check_book()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page=ProductPage(browser, PRODUCT_PAGE_LINK)
    page.open()
    page.btn_add_to_basket_find()
    page.btn_add_to_basket_click()
    page.should_be_alert_inners()
    page.check_price_from_alerts()
    page.check_book()
    
@pytest.mark.xfail 
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page=ProductPage(browser, PRODUCT_PAGE_LINK)
    page.open()
    page.btn_add_to_basket_find()
    page.btn_add_to_basket_click()
    page.check_success_message_presence()
 

def test_guest_cant_see_success_message(browser): 
    page=ProductPage(browser, PRODUCT_PAGE_LINK)
    page.open()
    page.check_success_message_presence()

@pytest.mark.xfail 
def test_message_disappeared_after_adding_product_to_basket(browser): 
    page=ProductPage(browser, PRODUCT_PAGE_LINK)
    page.open()
    page.btn_add_to_basket_find()
    page.btn_add_to_basket_click()
    page.check_success_message_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    page=ProductPage(browser,PRODUCT_TEST_LOGIN_LINK)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page=ProductPage(browser, PRODUCT_PAGE_LINK)
    page.open()
    page.go_to_login_page()
    page.check_login_was_successful()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page=ProductPage(browser, PRODUCT_PAGE_LINK)
    page.open()
    page.button_basket_press()
    page.check_basket_is_empty()
    page.check_basket_has_empty_message()

@pytest.mark.user_tests
class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture
    def setup(self, browser):
        page=LoginPage(browser, PRODUCT_PAGE_LINK)
        page.open()
        page.go_to_login_page()
        page.check_login_was_successful()
        email=str(time.time())+"@somemail.com"
        password="Stepic12345cipetS"
        page.register_new_user(email,password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, setup, browser): 
        page=ProductPage(browser, PRODUCT_PAGE_LINK)
        page.open()
        page.check_success_message_presence()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, setup, browser):
        page=ProductPage(browser, PRODUCT_PAGE_LINK)
        page.open()
        page.btn_add_to_basket_find()
        page.btn_add_to_basket_click()
        page.should_be_alert_inners()
        page.check_price_from_alerts()
        page.check_book()