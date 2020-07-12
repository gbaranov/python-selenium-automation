from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

COLOR_NAME = (By.CSS_SELECTOR, 'span.selection')
COLOR_BLOCKS = (By.CSS_SELECTOR, 'ul.swatches li')
SELECTED_COLOR = (By.CSS_SELECTOR, 'div#variation_color_name span.selection')


@given('Open Amazon product by ASIN {id}')
def open_by_asin(context, id):
    context.driver.get(f'https://www.amazon.com/gp/product/{id}/')


@then('User can select through colors')
def verify_color_selection(context):
    expected_colors = ['Black', 'Blue Overdyed', 'Dark Wash', 'Indigo Wash', 'Light Wash', 'Medium Wash', 'Rinse', 'Vintage Light Wash']
    color_options = context.driver.find_elements(*COLOR_BLOCKS)
    for color in color_options:
        color.click()
        assert context.driver.find_element(*SELECTED_COLOR).text == expected_colors[color_options.index(color)]
