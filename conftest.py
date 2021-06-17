"""
Тесты напсианы и работают для FireFox
"""
import time
import pytest
from selenium import webdriver

supported_languages = ['en', 'ru', 'es', 'fr']


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose browser's language: en, ru, fr, es")


@pytest.fixture(scope='module')
def browser(request):
    browser_lang = request.config.getoption('language')
    if browser_lang not in supported_languages:
        raise pytest.UsageError("--language should be 'en, ru, fr, es' ")
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", browser_lang)
    browser = webdriver.Firefox(firefox_profile=fp)
    browser.implicitly_wait(5)
    yield browser
    time.sleep(30)
    browser.quit()


@pytest.fixture(scope='module')
def browser_lg(request):
    language = request.config.getoption('language')
    yield language
