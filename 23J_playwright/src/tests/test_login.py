from playwright.sync_api import Page,expect


def test_login_with_StandardUser(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")