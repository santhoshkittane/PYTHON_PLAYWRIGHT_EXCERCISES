import re
import pytest



from playwright.sync_api import Page, expect

@pytest.mark.smoke
def test_homepage_has_correct_title(page: Page):
    # 1. Navigate to the website
    page.goto("https://playwright.dev/")

    # 2. Assert the title contains a specific substring
    expect(page).to_have_title(re.compile("Playwright"))

@pytest.mark.integration
def test_click_get_started(page: Page):
    # 1. Navigate to the website
    page.goto("https://playwright.dev/")

    # 2. Click the 'Get started' link using a locator
    page.get_by_role("link", name="Get started").click()

    # 3. Assert that the page displays the 'Installation' heading
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


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
