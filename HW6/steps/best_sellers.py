from behave import when, then, given
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

BEST_SELLERS = (By.LINK_TEXT, 'Best Sellers')
TABS = (By.XPATH, '//*[@id="zg_tabs"]/ul/li')
TABS_BLOCK = (By.CSS_SELECTOR, 'div#zg_tabs')
LINKS_ARRAY = []


@when('Click Best Sellers')
def click_best_sellers(context):
    context.driver.find_element(*BEST_SELLERS).click()


@when('Open page and verify title')
def links(context):
    tabs = context.driver.find_elements(*TABS)
    for tab in tabs:
        LINKS_ARRAY.append(tab.text)
    for link in LINKS_ARRAY:
        tabs_block = context.driver.find_element(*TABS_BLOCK)
        tabs_block.find_element_by_link_text(link).click()
        context.driver.wait.until(EC.title_contains(link))