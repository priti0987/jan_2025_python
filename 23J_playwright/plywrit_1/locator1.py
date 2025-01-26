from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    # page = browser.new_page()
    # page.goto("https://demo.automationtesting.in/")

    #id edit-name
    # email_id = page.wait_for_selector('#email')
    # email_id.type('test@gmail.com')
    # button= page.wait_for_selector('#enterimg')
    # button.click()
    # page.wait_for_timeout(2000)
    # browser.close()
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username = page.wait_for_selector('input[name=username]')
    username.type('Admin')
    password_=page.wait_for_selector('input[name=password]')
    password_.type('admin123')
    btnlogin = page.wait_for_selector('button[type=submit]')
    btnlogin.click()
    page.wait_for_timeout(2000)


