from behave import when, then, given
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

BLOG_LINK = (By.XPATH, "//a[contains(text(), 'See daily updates at blog.aboutamazon.com')]")
#It's parent div has dynamically generated id, no way to catch it.
#Also page use similar structure with it's classes for other blocks
#Gotta use full xpath or using contains()
BLOG_TITLE = (By.XPATH, "//html/head/title[contains(text(), 'blog')]")
BLOG_MENU = (By.CSS_SELECTOR, "button.ArticlePage-header-menuToggle")
BLOG_MENU_CLOSE = (By.CSS_SELECTOR, 'button.ArticlePage-header-menuClose')


@when('Store original windows')
def store_windows(context):
    context.original_windows = context.driver.window_handles


@when("Click on blog link See daily updates at blog.aboutamazon.com")
def blog(context):
    context.driver.find_element(*BLOG_LINK).click()
    sleep(5)


@when("Switch to the newly opened window")
def switch(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    context.driver.switch_to_window(current_windows[1])
    print(current_windows)


@then("Amazon Blog is opened")
def verify_blog(context):
    context.driver.find_element(*BLOG_TITLE)


@then("User can open and close Blog menu")
def open_close(context):
    context.driver.find_element(*BLOG_MENU).click()
    context.driver.wait.until(EC.visibility_of_element_located(BLOG_MENU_CLOSE))
    context.driver.find_element(*BLOG_MENU_CLOSE).click()
    context.driver.wait.until(EC.invisibility_of_element_located(BLOG_MENU_CLOSE))


@then('User can close new window and switch back to original')
def close_window(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_windows[0])
    sleep(10)