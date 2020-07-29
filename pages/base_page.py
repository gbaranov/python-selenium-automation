from selenium.webdriver.support.wait import WebDriverWait

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.amazon.com/'
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self, url=''):
        self.driver.get(self.base_url + url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)
