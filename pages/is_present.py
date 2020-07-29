from pages.base_page import Page
from selenium.webdriver.common.by import By

class isPresent(Page):

    LOGIN_FORM = (By.CSS_SELECTOR, "div.a-section.auth-pagelet-container")
    CART_IS_EMPTY_SIGN = (By.XPATH, "//*[@id='sc-active-cart']/div/div[2]/div[1]")
    AMAZON_MUSIC_MENU_ITEMS = (By.XPATH, '//*[@id="hmenu-content"]/ul[3]/li/a')


    def signin_is_present(self):
        login = self.find_element(*self.LOGIN_FORM)
        return login

    def cart_is_empty_is_present(self, expected_text):
        result = self.find_element(*self.CART_IS_EMPTY_SIGN).text
        assert expected_text in result , "Expected word '{}' in message, but got '{}'".format(expected_text, result)

    def amazon_music_6_items_is_present(self):
        test = self.find_elements(*self.AMAZON_MUSIC_MENU_ITEMS)
        for t in test:
            print(t.text)
