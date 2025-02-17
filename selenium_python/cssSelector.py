#tag = id
#tag = class
#tag =attribute
#tag = class and attribute
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.facebook.com/"
driver.get(url)
driver.maximize_window()
time.sleep(2)
#id
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("priti")
driver.find_element(By.CSS_SELECTOR,"#email").send_keys("priti")
time.sleep(2)
print("done....")

#class
driver.find_element(By.CSS_SELECTOR,"")
