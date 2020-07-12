from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

OFFERS = (By.XPATH, "//*[@id='wfm-pmd_deals_section']/div[6]/ul/li")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'span.a-size-medium.wfm-sales-item-card__product-name.a-text-bold')
PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.a-size-small.a-color-tertiary.wfm-sales-item-card__regular-price')
#Had to reffer by XPATH because the offers ul/li structure on top of the page
#is identical. No any unique class or ID specifically for the bottom part.

@given('Open Whole Foods deals page')
def open_deals_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')

@then('Verify each product has Title and Regular')
def validation(context):
    offers_parsed = context.driver.find_elements(*OFFERS)
    for i in range(len(offers_parsed)):
        try:
            if offers_parsed[i].find_element(*PRODUCT_TITLE).text:
                name = offers_parsed[i].find_element(*PRODUCT_TITLE).text
                print("Item number ", i+1, " Title found: ", name)
            else:
                print("Item number ", i+1, "Title not found")
            if offers_parsed[i].find_element(*PRODUCT_PRICE).text:
                price = offers_parsed[i].find_element(*PRODUCT_PRICE).text
                if "Regular" in price:
                    print("Contains - Regular")
            else:
                print("Doesn't Contain - Regular")
        except:
            print("Item number ", i+1, " Block doesn't match the requirements")


