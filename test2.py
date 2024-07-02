from playwright.sync_api import sync_playwright
import config

def get_all_links():
    full_links = []

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            # Navigate to the login page
            page.goto("https://codecourse.com/")
            page.click('//nav//a[contains(text(), "Sign in")]')

            # Perform login
            page.fill('input[name="email"]', config.LOGIN_EMAIL)
            page.fill('input[name="password"]', config.LOGIN_PASSWORD)
            page.click('button[type="submit"]')

            # Wait for navigation after login
            page.wait_for_load_state('networkidle')

            # Construct the course URL and navigate to the course page
            course_url = f"{config.COURSE_BASE_URL}{config.COURSE_SLUG}"
            page.goto(course_url)

            # Wait for the episode links to load
            page.wait_for_selector('a')
            episode_links = page.query_selector_all('a[href*="watch"]')

            links = [link.get_attribute('href') for link in episode_links]
            full_links = [f"https://codecourse.com{link}" for link in links]

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            browser.close()

        return full_links





if __name__ == "__main__":
    links = get_all_links()
    if not links:
        print("No links found or an error occurred.")
    else:
        for link in links:
            print(link)


