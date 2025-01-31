#open browser
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://admin-demo.nopcommerce.com/admin/")
    username = page.wait_for_selector("//input[@id='Email']")
    username.fill("")
    username.type('admin@yourstore.com')
    password_ = page.wait_for_selector("//input[@id='Password']")
    password_.fill("")
    password_.type('admin')
    btnlogin = page.wait_for_selector('button[type=submit]')
    btnlogin.click()
    #
    print(page.title())
    page.wait_for_timeout(30000)
