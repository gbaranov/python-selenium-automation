from pages.base_page import Page
from pages.top_nav_menu import TopNavMenu
from pages.search_results import SearchResults

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.page = Page(self.driver)
        self.top_nav_menu = TopNavMenu(self.driver)
        self.search_results = SearchResults(self.driver)