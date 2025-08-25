import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.fixture
def setup_swaglabs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")

        yield page
        page.close()
        browser.close()
        print("End Test")