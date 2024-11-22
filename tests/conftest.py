import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def set_up():
    print("--START TEST--")
    options = Options()
    driver = webdriver.Chrome(options=options)
    url = 'https://www.litres.ru/'
    driver.get(url)
    driver.maximize_window()
    yield driver
    print("--FINISH TEST--")
