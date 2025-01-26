from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #xpath relative xpath
    username_ele = page.wait_for_selector("//input[@name='username']")
    password_ele = page.wait_for_selector("//input[@name='password']")
    loginbtn = page.wait_for_selector("//button[@type='submit']")
    userName= page.get_by_text("//p[@class='oxd-text oxd-text--p'][1]")
    print(userName.get_attribute('text'))
    # username_ele.type('Admin')
    # password_ele.type('admin123')
    # loginbtn.click()
    # page.wait_for_timeout(3000)
