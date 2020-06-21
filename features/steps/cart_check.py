from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Amazon page')
def open_amazon_page(context):
    context.driver.get('https://amazon.com')
@when('Click on Cart icon')
def open_cart(context):
    context.driver.find_element(By.ID, 'nav-cart').click()
    sleep(2)
@then('Verify Cart is Empty')
def cart_verif(context):
    cart_data = context.driver.find_element(By.ID, 'sc-active-cart')
    assert "Your Amazon Cart is empty" in cart_data.text
