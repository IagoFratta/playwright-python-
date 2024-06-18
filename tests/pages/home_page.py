# pages/home_page.py
from .base_page import BasePage
from config import BASE_URL

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = BASE_URL
    
    def open(self):
        self.goto(self.url)
