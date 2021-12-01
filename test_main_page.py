import time
import pytest

def test_guest_can_go_to_login(browser, language):
    link="http://selenium1py.pythonanywhere.com/"
    browser.implicitly_wait(10)
    browser.get(link)
    login_link=browser.find_elements_by_css_selector("#login_link")