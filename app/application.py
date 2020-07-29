from pages.base_page import Page
from pages.top_nav_menu import TopNavMenu
from pages.search_results import SearchResults
from pages.is_present import isPresent
from pages.hamburger_nav import HamburgerNav

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.page = Page(self.driver)
        self.top_nav_menu = TopNavMenu(self.driver)
        self.search_results = SearchResults(self.driver)
        self.is_present = isPresent(self.driver)
        self.hamburger_nav = HamburgerNav(self.driver)
