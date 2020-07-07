from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
import re

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.CSS_SELECTOR, 'input.nav-input')
ITEM_TITLE = (By.CSS_SELECTOR, 'a.a-link-normal.a-text-normal')
ADD_TO_CART = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart')
ITEM_TITLE_IN_CART = (By.CLASS_NAME, 'a-size-medium.sc-product-title.a-text-bold')
SELECTED_ITEMS = []
CART_ITEMS_OBJECTS = []
CART_ITEMS_TEXT = []
#ASIN = (By.CSS_SELECTOR, 'a.a-link-normal.a-text-normal')


@given('Open Amazon page')
def open_amazon_page(context):
    context.driver.get('https://amazon.com')


@when('Input {query} into search field')
def search_input(context, query):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(query)
    button = context.driver.find_element(*SEARCH_BUTTON)
    button.click()
    sleep(2)


@when('Click on item title')
def title_click(context):
    item_title = context.driver.find_element(*ITEM_TITLE)
#    item_asin_link = context.driver.find_element(*ASIN).get_attribute('href')
#    print(item_asin_link)
#    pattern = "dp\/(.*?)\/"
#    substring = re.search(pattern, item_asin_link)
#    print(substring)
    print(item_title.text)
    SELECTED_ITEMS.append(item_title.text)
    item_title.click()
    sleep(1)


@when('Click add to cart')
def title_click(context):
    context.driver.find_element(*ADD_TO_CART).click()
    sleep(2)


@when('Click Cart')
def cart_click(context):
    context.driver.find_element(*CART).click()
    sleep(1)


# Ok, here's the problem i ran into. To verify if the cart contains correct items selected by user,
# there's couple ways to do it.
# I was unable to match title of selected item with title in a cart, because they're all written different
# (search results, product page, cart). Was thinking about check for 3+ matching words, but it makes
# complicated algorithm and it won't work properly if all products has similar titles
# Smartest way, use the item ASIN, but if you'll check search results, you may notice some listings
# like Promoted and sold by Amazon, has different url structure. Then it has to parsed from it's parent
# attributes <div data-asin="B072LN1L1X". Will try to implement in further assignments



@then('Item is shown')
def cart_check(context):
    CART_ITEMS_OBJECTS = context.driver.find_elements(*ITEM_TITLE_IN_CART)
    print("Cart items:")
    for text in CART_ITEMS_OBJECTS:
        CART_ITEMS_TEXT.append(text.get_attribute('innerHTML').strip())
        print(text.get_attribute('innerHTML').strip())
    print("Total items in cart: " + str(len(CART_ITEMS_TEXT)))

#Shows items in cart and total amount
#Works with multiple items added
