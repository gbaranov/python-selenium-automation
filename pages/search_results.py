from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResults(Page):
    RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]")

    def verify_found_results_text(self, search_word):
        results_msg = self.find_element(*self.RESULTS_FOUND_MESSAGE).text
        assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)
