import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = None

@pytest.fixture(scope='module')
def initDriver():
    print("------------------ INIT DRIVER -------------------")
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.cleartrip.com")
    yield
    print("----------------------- END ------------------------------")
    time.sleep(2)
    driver.quit()

@pytest.mark.usefixtures("initDriver")
def test_google_title():
    time.sleep(2)
    print(driver.title)
    assert driver.title == 12

def test_google_url(initDriver):
    time.sleep(2)
    print(driver.current_url)
