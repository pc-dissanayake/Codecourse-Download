import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

def test_open_google(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")
    assert "Google" in page.title()
    context.close()
