from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.common.by import By

class HamburgerNav(Page):
    AMAZON_MUSIC = (By.XPATH, '//*[@id="hmenu-content"]/ul[1]/li[3]/a')
    MUSIC_MENU = (By.ID, 'hmenu-content')
    MUSIC_MENU_SELECTIONS = (By.CSS_SELECTOR, 'a.hmenu-item')


    def amazon_music_click(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.AMAZON_MUSIC))
        self.click(*self.AMAZON_MUSIC)
