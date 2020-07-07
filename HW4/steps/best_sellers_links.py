from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BEST_SELLERS_LINK = (By.XPATH, "//*[@id='nav-xshop']/a[1]")

BEST_SELLERS = (By.XPATH, "//*[@id='zg_tabs']/ul/li[1]/div/a")
NEW_RELEASES = (By.XPATH, "//*[@id='zg_tabs']/ul/li[2]/div/a")
MOVERS_SHAKERS = (By.XPATH, "//*[@id='zg_tabs']/ul/li[3]/div/a")
MOST_WISHED_FOR = (By.XPATH, "//*[@id='zg_tabs']/ul/li[4]/div/a")
GIFT_IDEAS = (By.XPATH, "//*[@id='zg_tabs']/ul/li[5]/div/a")

@when('Click Best Sellers link')
def bs_click(context):
    context.driver.find_element(*BEST_SELLERS_LINK).click()
    sleep(2)


@then('Verify links existence')
def link_check(context):
    print(context.driver.find_element(*BEST_SELLERS).get_attribute("text"))
    print(context.driver.find_element(*NEW_RELEASES).get_attribute("text"))
    print(context.driver.find_element(*MOVERS_SHAKERS).get_attribute("text"))
    print(context.driver.find_element(*MOST_WISHED_FOR).get_attribute("text"))
    print(context.driver.find_element(*GIFT_IDEAS).get_attribute("text"))