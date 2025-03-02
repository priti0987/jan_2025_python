import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = None

def setup_module(module):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.cleartrip.com")

def teardown_module(module):
    time.sleep(2)
    driver.quit()

def test_google_title():
    time.sleep(2)
    print(driver.title)
    assert driver.title

def test_google_url():
    time.sleep(2)
    print(driver.current_url)
