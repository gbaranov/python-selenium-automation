
from selenium.webdriver.common.by import By
from behave import given, when, then


RESULTS = (By.XPATH, "//div[@class='g']")


@given('Open Google page')
def open_google(context):
    #context.driver.get('https://www.google.com/')
    context.app.page.open_page()

@when('Input {search_word} into search field and Click on search icon')
def input_search(context, search_word):
    #search = context.driver.find_element(*SEARCH_INPUT)
    #search.clear()
    #search.send_keys(search_word)
    #sleep(4)
    context.app.top_nav_menu.search_word(search_word)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    context.app.search_results.verify_found_results_text(search_word)