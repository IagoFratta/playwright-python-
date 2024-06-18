import pytest
from pytest_bdd import scenarios, given, then
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage

# Carregar os cenários do arquivo .feature
scenarios('../features/example.feature')

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@given('I open the homepage')
def open_homepage(browser):
    home_page = HomePage(browser)
    home_page.open()

@then('I should see the homepage title')
def see_homepage_title(browser):
    home_page = HomePage(browser)
    assert home_page.get_title() == 'awdawd'
