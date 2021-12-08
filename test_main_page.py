from .pages.main_page import MainPage
import pytest
MAIN_PAGE_LINK="https://selenium1py.pythonanywhere.com/en-gb/catalogue/"


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page=MainPage(browser, MAIN_PAGE_LINK)
    page.open()
    page.button_basket_press()
    page.check_basket_is_empty()
    page.check_basket_has_empty_message()


@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page_from_main_page(self, browser):
        page=MainPage(browser, MAIN_PAGE_LINK)
        page.open()
        page.go_to_login_page()
        page.check_login_was_successful()

    def test_schold_see_login_link_from_main_page(self, browser):
        page=MainPage(browser,MAIN_PAGE_LINK)
        page.open()
        page.should_be_login_link()

