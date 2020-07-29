from pages.base_page import Page
from selenium.webdriver.common.by import By

class TopNavMenu(Page):
    ORDERS = (By.ID, 'nav-orders')
    CART = (By.ID, 'nav-cart')
    HAMBURGER = (By.ID, 'nav-hamburger-menu')
    HAMBURGER_UL = (By.CSS_SELECTOR, 'ul.hmenu.hmenu-visible')

    def orders_click(self):
        self.click(*self.ORDERS)

    def cart_click(self):
        self.click(*self.CART)

    def hamburger_click(self):
        self.click(*self.HAMBURGER)

