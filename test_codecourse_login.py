import pytest
from playwright.sync_api import sync_playwright
import config  # Import the configuration file


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        # Do not close the context or browser to keep the browser open
        # context.close()
        # browser.close()


def test_codecourse_xpath(browser):
    page = browser

    # Navigate to the specific course URL
    page.goto(config.COURSE_URL)

    # Perform your actions on the course page
    # Example actions:
    page.click('button[name="start_course"]')
    page.wait_for_selector('text=Next Lesson')
    page.click('text=Next Lesson')

    # Extract and print all URLs on the page
    anchors = page.query_selector_all('a')
    urls = [anchor.get_attribute('href') for anchor in anchors]

    for url in urls:
        print(url)

    # Keep the browser open by not closing the context or browser


if __name__ == "__main__":
    pytest.main()
