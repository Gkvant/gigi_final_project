import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.fixture
def setup_jw_org():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.jw.org/en/")

        yield page
        page.close()
        browser.close()
