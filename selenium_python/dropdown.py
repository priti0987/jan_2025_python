from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

url = "https://demo.automationtesting.in/Register.html"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

#select
select_web = driver.find_element(By.XPATH,"//select[@id='Skills']")
select_1 = Select(select_web)
select_1.select_by_index(4)
time.sleep(3)
select_1.select_by_value("APIs")
time.sleep(3)
select_1.select_by_visible_text("AutoCAD")
time.sleep(3)