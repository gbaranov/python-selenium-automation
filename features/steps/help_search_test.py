from selenium import webdriver
from selenium.webdriver.common.by import By

import time

#preset
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.amazon.com/gp/help/customer/display.html')

searchform = driver.find_element(By.ID, 'helpsearch')
searchform.clear()
searchform.send_keys('cancel order')

gobutton = driver.find_element(By.CLASS_NAME, 'a-button-input')
gobutton.click()
time.sleep(3)

if('cancel order' in driver.page_source):
    print("Search results reached")


driver.quit()