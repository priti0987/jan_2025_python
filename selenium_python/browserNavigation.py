from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

url = "https://demo.automationtesting.in/Register.html"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

time.sleep(2)
driver.get("https://www.google.com")
time.sleep(2)
driver.back()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.forward()
