from behave import when, then, given
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

POPUP = (By.CSS_SELECTOR, '#nav-signin-tooltip span')

@given('Open Amazon page')
def open_amazon_page(context):
    context.driver.get('https://amazon.com')


@then('Verify Sign in popup is present and clickable')
def popup_present_clickable(context):
    context.driver.wait.until(EC.presence_of_element_located(POPUP))
    context.driver.wait.until(EC.element_to_be_clickable(POPUP))


@when('Sign in popup disappears')
def invisible_popup(context):
    context.driver.wait.until(EC.invisibility_of_element(POPUP))


@then('Verify Sign in popup is not clickable')
def unclickable_popup(context):
    context.driver.wait.until_not(EC.element_to_be_clickable(POPUP))