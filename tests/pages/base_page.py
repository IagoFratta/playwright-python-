from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def wait_for_selector(self, selector: str):
        self.page.wait_for_selector(selector)
