import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Это значит, что параметр language обязателен для запуска данного теста
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language please")

# Это фикстура в которой открывается браузер с учетом языка, который ввел пользователь
@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    # Получаем значение параметра language из командной строки
    user_language = request.config.getoption("language")
    options = Options()
    # Запускаем браузер с языком, который выбрали
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()