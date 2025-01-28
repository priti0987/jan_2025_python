from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #xpath relative xpath
    username_ele = page.wait_for_selector("//input[@name='username']")
    password_ele = page.wait_for_selector("//input[@name='password']")
    loginbtn = page.wait_for_selector("//button[@type='submit']")
    userName= page.inner_text("//p[@class='oxd-text oxd-text--p'][1]")
    username = (userName.split(":")[1]).strip()
    username_ele.type(username)
    password= page.inner_text("//p[@class='oxd-text oxd-text--p'][2]")
    password = (password.split(":")[1]).strip()
    password_ele.type(password)
    loginbtn.click()
    page.wait_for_timeout(3000)
