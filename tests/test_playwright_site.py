"""
Pytest + Playwright test suite for https://playwright.dev/

Covers: navbar links, hero section, product cards, feature links,
footer links, theme toggle, search modal, external link behavior,
responsive layout, and basic a11y/broken-link checks.

Setup (run once):
    pip install pytest-playwright
    playwright install chromium

Run:
    pytest test_playwright_site.py -v
    pytest test_playwright_site.py -v -k "footer"     # run a subset
    pytest test_playwright_site.py -v --headed        # watch it run
"""

import re
import pytest
from playwright.sync_api import expect, Page, BrowserContext

BASE_URL = "https://playwright.dev/"


@pytest.fixture(autouse=True)
def go_home(page: Page):
    """Every test starts from the homepage."""
    page.goto(BASE_URL)


# ---------------------------------------------------------------------------
# 1. Top navigation bar
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "link_name,url_fragment",
    [
        ("Docs", "/docs/intro"),
        ("MCP", "/mcp/introduction"),
        ("CLI", "/agent-cli/introduction"),
        ("API", "/docs/api/class-playwright"),
    ],
)
def test_navbar_link_navigates(page: Page, link_name, url_fragment):
    page.get_by_role("link", name=link_name, exact=True).click()
    expect(page).to_have_url(re.compile(re.escape(url_fragment)))


def test_logo_navigates_home(page: Page):
    page.get_by_role("link", name=re.compile("Docs")).click()  # go elsewhere first
    page.get_by_role("link", name="Playwright logo Playwright").click()
    expect(page).to_have_url(BASE_URL)


def test_language_dropdown_opens(page: Page):
    page.get_by_role("button", name="Node.js").click()
    # Dropdown should reveal at least one other language option
    expect(page.get_by_role("link", name=re.compile("Python|\\.NET|Java"))).to_be_visible()


def test_theme_toggle_switches_mode(page: Page):
    html = page.locator("html")
    before = html.get_attribute("data-theme")
    page.get_by_role("button", name=re.compile("Switch between dark and light mode")).click()
    after = html.get_attribute("data-theme")
    assert before != after, f"Expected theme to change, stayed at {before}"


def test_search_modal_opens_and_closes(page: Page):
    page.get_by_role("button", name=re.compile("^Search")).click()
    search_input = page.get_by_placeholder(re.compile("Search", re.IGNORECASE))
    expect(search_input).to_be_visible()
    page.keyboard.press("Escape")
    expect(search_input).to_be_hidden()


def test_github_icon_opens_new_tab(page: Page, context: BrowserContext):
    with context.expect_page() as new_page_info:
        page.get_by_role("link", name="GitHub repository").click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    expect(new_page).to_have_url(re.compile("github.com/microsoft/playwright"))
    new_page.close()


def test_discord_icon_opens_new_tab(page: Page, context: BrowserContext):
    with context.expect_page() as new_page_info:
        page.get_by_role("link", name="Discord server").click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    assert "discord" in new_page.url.lower()
    new_page.close()


# ---------------------------------------------------------------------------
# 2. Hero section
# ---------------------------------------------------------------------------

def test_get_started_button(page: Page):
    page.get_by_role("link", name="Get started").click()
    expect(page).to_have_url(re.compile("/docs/intro"))


@pytest.mark.parametrize(
    "lang_name,url_fragment",
    [
        ("TypeScript", "/docs/intro"),
        ("Python", "/python/docs/intro"),
        (".NET", "/dotnet/docs/intro"),
        ("Java", "/java/docs/intro"),
    ],
)
def test_hero_language_links(page: Page, lang_name, url_fragment):
    page.get_by_role("link", name=lang_name, exact=True).first.click()
    expect(page).to_have_url(re.compile(re.escape(url_fragment)))


def test_stargazers_link(page: Page, context: BrowserContext):
    with context.expect_page() as new_page_info:
        page.get_by_role("link", name=re.compile("stargazers on GitHub")).click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    expect(new_page).to_have_url(re.compile("stargazers"))
    new_page.close()


# ---------------------------------------------------------------------------
# 3. Product cards (Test / CLI / MCP)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "link_name,url_fragment",
    [
        ("Testing documentation", "/docs/intro"),
        ("CLI documentation", "/docs/getting-started-cli"),
        ("MCP documentation", "/docs/getting-started-mcp"),
    ],
)
def test_product_card_links(page: Page, link_name, url_fragment):
    page.get_by_role("link", name=link_name).click()
    expect(page).to_have_url(re.compile(re.escape(url_fragment)))


# ---------------------------------------------------------------------------
# 4. Feature / tooling links
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "link_name,url_fragment",
    [
        ("Test generator", "codegen"),
        ("Trace Viewer", "trace-viewer-intro"),
        ("VS Code extension", "getting-started-vscode"),
    ],
)
def test_feature_heading_links(page: Page, link_name, url_fragment):
    page.get_by_role("link", name=link_name).click()
    expect(page).to_have_url(re.compile(re.escape(url_fragment)))


def test_mcp_external_link(page: Page, context: BrowserContext):
    with context.expect_page() as new_page_info:
        page.get_by_role("link", name="Model Context Protocol").click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    assert "modelcontextprotocol.io" in new_page.url
    new_page.close()


# ---------------------------------------------------------------------------
# 5. Footer links
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "link_name,should_open_new_tab",
    [
        ("Getting started", False),
        ("Stack Overflow", True),
        ("Discord", True),
        ("X", True),
        ("LinkedIn", True),
        ("GitHub", True),
        ("YouTube", True),
        ("Blog", True),
        ("Ambassadors", False),
    ],
)
def test_footer_links(page: Page, context: BrowserContext, link_name, should_open_new_tab):
    footer = page.locator("footer")
    link = footer.get_by_role("link", name=re.compile(re.escape(link_name))).first

    if should_open_new_tab:
        with context.expect_page() as new_page_info:
            link.click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        assert new_page.url, "Expected new tab to load a URL"
        new_page.close()
    else:
        link.click()
        expect(page).to_have_url(re.compile(r"playwright\.dev"))


# ---------------------------------------------------------------------------
# 6. Company logos
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "company",
    ["VS Code", "Bing", "Outlook", "Disney+ Hotstar", "Material UI",
     "ING", "Adobe", "React Navigation", "Accessibility Insights"],
)
def test_company_logo_links(page: Page, context: BrowserContext, company):
    link = page.get_by_role("link", name=company)
    expect(link).to_be_visible()
    href = link.get_attribute("href")
    assert href and href.startswith("http"), f"{company} logo missing a valid href"


# ---------------------------------------------------------------------------
# 7. Cross-cutting checks
# ---------------------------------------------------------------------------

def test_homepage_title(page: Page):
    expect(page).to_have_title(re.compile("Playwright"))


def test_keyboard_navigation_focuses_navbar(page: Page):
    page.keyboard.press("Tab")
    focused = page.evaluate("document.activeElement.tagName")
    assert focused in ("A", "BUTTON"), f"Expected focus on a link/button, got {focused}"


def test_responsive_mobile_layout(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})
    page.reload()
    # On mobile, main nav links are typically hidden behind a menu toggle
    expect(page.get_by_role("link", name="Playwright logo Playwright")).to_be_visible()


def test_no_broken_links_on_homepage(page: Page, context: BrowserContext):
    """Collect all hrefs on the homepage and verify each responds successfully."""
    hrefs = page.eval_on_selector_all(
        "a[href]",
        "els => els.map(e => e.href).filter(h => h.startsWith('http'))",
    )
    unique_hrefs = sorted(set(hrefs))[:15]  # cap to keep the test fast

    broken = []
    for href in unique_hrefs:
        try:
            response = context.request.get(href, timeout=10000)
            if response.status >= 400:
                broken.append((href, response.status))
        except Exception as e:
            broken.append((href, str(e)))

    assert not broken, f"Broken links found: {broken}"
