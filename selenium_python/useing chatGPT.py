# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
# # Set up the WebDriver (Ensure chromedriver.exe is in PATH)
# driver = webdriver.Chrome()
#
# # Open Facebook login page
# driver.get("https://www.facebook.com/")
#
# # Maximize browser window
# driver.maximize_window()
#
# # Locate username and password fields
# email_field = driver.find_element(By.ID, "email")
# password_field = driver.find_element(By.ID, "pass")
#
# # Enter login credentials
# email_field.send_keys("your-email@example.com")  # Replace with your email
# password_field.send_keys("your-password")        # Replace with your password
#
# # Submit login form
# password_field.send_keys(Keys.RETURN)
#
# # Wait for a few seconds to observe the result
# time.sleep(5)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Set up the WebDriver (Ensure chromedriver.exe is in PATH)
driver = webdriver.Chrome()

# Open a sample page with a dropdown (Replace with actual URL)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Maximize browser window
driver.maximize_window()

# Locate the dropdown element by its name, ID, or XPath
dropdown = driver.find_element(By.NAME, "my-select")  # Replace with actual dropdown locator

# Create a Select object
select = Select(dropdown)

# Select options in d
time.sleep(5)
