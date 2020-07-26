from pages.base_page import Page
from selenium.webdriver.common.by import By

class TopNavMenu(Page):
    SEARCH_INPUT = (By.NAME, 'q')
    SEARCH_SUBMIT = (By.NAME, 'btnK')

    def search_word(self, search_word):
        self.input(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_SUBMIT)
