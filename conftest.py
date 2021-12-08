import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
        help="Specify web page language")

@pytest.fixture(scope="function")
def browser(request):   
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()
