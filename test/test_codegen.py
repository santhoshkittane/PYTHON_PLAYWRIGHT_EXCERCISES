import pytest
import re
from playwright.sync_api import Page, expect

@pytest.mark.regression
def test_homepage_has_correct_title(page: Page):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="CLI", exact=True).click()
    page.get_by_role("link", name="Docs").click()
    page.get_by_role("link", name="Running and debugging tests").click()


    # context.close()
    # browser.close()
@pytest.mark.validation
def test_run(page: Page) -> None:
        # browser = playwright.chromium.launch(headless=False)
        # context = browser.new_context()
        # page = context.new_page()
        page.goto("https://www.google.com/")
        # page.get_by_role("link", name="About").click()
        # page.wait_for_timeout(3000)
        # current_url = page.url
        # print(current_url)
        # #expect(current_url.__contains__("google"))
        expect(page).to_have_url(re.compile(r"google"))
        gmail_link = page.get_by_role("link", name="Gmail")
        gmail_link.click()
        expect(page).to_have_url(re.compile(r"gmail"))



        # ---------------------
        # context.close()
        # browser.close()



