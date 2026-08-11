from playwright.sync_api import sync_playwright 

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    website = browser.new_page()
    website.goto("https://quotes.toscrape.com/login")
    website.fill("#username", "nwm")
    website.fill("#password", "nwmww12")
    website.click("input[type='submit']")
    website.wait_for_timeout(3000)
    browser.close()
