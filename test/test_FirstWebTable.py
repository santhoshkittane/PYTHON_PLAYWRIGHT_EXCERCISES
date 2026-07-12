import re
import pytest
from playwright.sync_api import expect, Page, BrowserContext

BASE_URL = "https://practice-automation.com/tables/"


@pytest.fixture(autouse=True)
def go_home(page: Page):
    """Every test starts from the homepage."""
    page.goto(BASE_URL)


def test_webtable(page:Page):
    table = page.locator("table").first
    rows = table.locator("tr")
    expect(rows).to_have_count(4)  # 1 header row + 4 data rows

    for i in range(rows.count()):
        cells = rows.nth(i).locator("td")
        if cells.count()>0 and cells.nth(0).inner_text() == "oranges":
            expect(cells.nth(1)).to_have_text("$3.99")
            page.screenshot(path=f"./row_{i}.png") 
            print(f"Screenshot saved for row {i} with 'oranges'")  
            break