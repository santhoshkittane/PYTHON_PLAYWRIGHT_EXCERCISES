import re
import pytest
from datetime import datetime



from playwright.sync_api import Page, expect

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

'''
This is to test
multiline comments
'''

@pytest.mark.smoke
def test_homepage_has_correct_title(page: Page):
    # 1. Navigate to the website
    page.goto("https://playwright.dev/")

    # 2. Assert the title contains a specific substring
    expect(page).to_have_title(re.compile("Playwright"))

#@pytest.mark.skip
@pytest.mark.smoke
def test_click_get_started(page: Page):
    # 1. Navigate to the website
    page.goto("https://playwright.dev/")
    #page.screenshot(path=f"screenshot{timestamp}.png")

    # 2. Click the 'Get started' link using a locator
    #page.get_by_role("link", name="Get started").click()
    link = page.get_by_role("link", name="Get started")
    link.click()
    #link.screenshot(path=f"Link-screenshot{timestamp}.png")

    # 3. Assert that the page displays the 'Installation' heading
    try:
        expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    except:
        page.screenshot(path=f"Fail-screenshot{timestamp}.png")
    page.screenshot(path=f"screenshot{timestamp}.png")



#@pytest.mark.xfail(reason="not Ready")
@pytest.mark.regression
def test_click_get_started_2(page: Page):
    # 1. Navigate to the website
    page.goto("https://playwright.dev/")
    #assert page.is_visible("text=fake")

    # 2. Click the 'Get started' link using a locator
    page.get_by_role("link", name="Get started").click()

    # 3. Assert that the page displays the 'Installation' heading
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
