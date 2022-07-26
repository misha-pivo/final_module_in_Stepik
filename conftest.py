import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru", help='Choose language')


@pytest.fixture(scope="function")
def driver(request):

    driver_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': driver_language})
    driver = webdriver.Chrome(executable_path=r"D:\stepik_selenium_course\chromeDriver\chromedriver.exe", options=options)

    yield driver
    print("\nquit browser..")
    driver.close()