from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Amazon page')
def open_amazon_page(context):
    context.driver.get('https://amazon.com')

@then("Locate Hamburger menu")
def locate_item(context):
    context.driver.find_element(By.ID, "nav-hamburger-menu")