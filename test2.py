from playwright.sync_api import sync_playwright

def get_episode_links():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://codecourse.com/courses/build-an-appointment-booking-system-with-livewire/")

        # Wait for the episode links to load
        page.wait_for_selector('a[href^="/watch/build-an-appointment-booking-system-with-livewire/"]')
        episode_links = page.query_selector_all('a[href^="/watch/build-an-appointment-booking-system-with-livewire/"]')

        links = [link.get_attribute('href') for link in episode_links]
        full_links = [f"https://codecourse.com{link}" for link in links]

        browser.close()
        return full_links

if __name__ == "__main__":
    links = get_episode_links()
    for link in links:
        print(link)
