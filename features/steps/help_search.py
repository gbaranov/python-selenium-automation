from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


HELP_SEARCH_INPUT = (By.ID, 'helpsearch')
SEARCH_SUBMIT = (By.CSS_SELECTOR, 'input.a-button-input')
RESULTS = (By.XPATH, "//div[@class='cs-help-content']")


#@given('Open Amazon Help page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


#@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*HELP_SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


#@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


#@then('Results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    results_msg = context.driver.find_element(*RESULTS).text
    #print(results_msg)
    assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)

