from selenium import webdriver
import time

from selenium.webdriver.common.by import By

url = "https://demo.automationtesting.in/Register.html"
driver = webdriver.Chrome()
driver.get(url)
#radio button
driver.find_element(By.XPATH,"//input[@value='FeMale']").click()

#checkbox and get attribute

li = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for el in li:
    val = el.get_attribute("value")
    print(val)
    if val == "Movies":
        el.click()
time.sleep(3)