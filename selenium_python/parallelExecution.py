import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_google():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    url = "https://www.saucedemo.com/"
    driver.get(url)
    driver.maximize_window()

def test_ICICIBank():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    url = "https://www.icicibank.com/"
    driver.get(url)
    driver.maximize_window()

def test_HDFCBANK():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    url = "https://www.hdfcbank.com/"
    driver.get(url)
    driver.maximize_window()

def test_YATRA():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    url = "https://www.yatra.com/"
    driver.get(url)
    driver.maximize_window()
