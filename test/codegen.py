from playwright.sync_api import Page, expect


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



