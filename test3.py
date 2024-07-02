from time import sleep
from urllib.parse import parse_qs

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # login
    browser = p.chromium.launch()
    context = browser.new_context(storage_state='/tmp/state.json')
    page = context.new_page()
    page.goto('https://demo.opencart.com/admin')
    page.fill('input#input-username', 'demo')
    page.fill('input#input-password', 'demo')
    page.click('button[type=submit]')
    sleep(5)  # just wait for redirect - you can wait for a element...
    page.context.storage_state(path='/tmp/state.json')
    page.screenshot(path='/tmp/after_state_init.png')
    # parse user_token for GET requests
    parsed_url = parse_qs(page.url)
    user_token = parsed_url['user_token'][0]
    print(f'user token {user_token}')
    page.close()
    browser.close()


with sync_playwright() as p:
    # open admin dashboard without login...
    browser = p.chromium.launch()
    context = browser.new_context()
    page = browser.new_page(storage_state='/tmp/state.json')
    page.goto(f'https://demo.opencart.com/admin/index.php?route=common/dashboard&user_token={user_token}')
    sleep(5)
    page.screenshot(path='/tmp/open_using_saved_state.png')
    page.close()
    browser.close()