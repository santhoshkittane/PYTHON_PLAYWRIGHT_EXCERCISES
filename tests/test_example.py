import re
import pytest
from datetime import datetime


from playwright.sync_api import Page, expect

@pytest.mark.sanity
def test_has_title(page: Page):
    # Navigate to the official Playwright homepage
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring
    #expect(page).to_have_title("Playwright")
    Page_title = page.title()
    print(Page_title)
    expect(page).to_have_title(re.compile(r"Playwright$"))

@pytest.mark.regression
def test_get_started_link(page: Page):
    # Navigate to the site
    page.goto("https://playwright.dev/")

    # Click the 'Get started' link
    page.get_by_role("link", name="Get started").click()

    # Expects URL to contain "intro"
    expect(page).to_have_url("https://playwright.dev/docs/intro")