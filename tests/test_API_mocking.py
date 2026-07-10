import json
import re
import pytest
from datetime import datetime


from playwright.sync_api import Page, expect # type: ignore

fruits = [
    {"id": 1, "name": "CYPRESS", "color": "Red"},
    {"id": 2, "name": "WebDriverIO", "color": "Blue"},
    {"id": 3, "name": "Orange", "color": "Orange"},
]

def test_mock_api_response(page: Page):
    # Mock the API response for a specific endpoint
    page.route("**/api/v1/fruits", lambda route: route.fulfill(
        status=200,
        content_type="application/json",
        body=json.dumps(fruits)
    ))

    # Navigate to the page that makes the API call
    page.goto("https://demo.playwright.dev/api-mocking/")
    #page.screenshot(path="screenshot.png")
    page.wait_for_timeout(5000)

    # expect(page.get_by_text("Cypress")).to_be_visible()
    # expect(page.get_by_text("WebDriverIO")).to_be_visible()