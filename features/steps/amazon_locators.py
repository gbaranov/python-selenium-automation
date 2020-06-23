from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-link-accountList').click()
time.sleep(3)


if driver.find_element(By.CLASS_NAME, 'a-link-nav-icon'):
    print("Logo found")
if driver.find_element(By.ID, 'ap_email'):
    print("Email form found")
if driver.find_element(By.ID, 'continue'):
    print("Continue button found")
if driver.find_element(By.CSS_SELECTOR, ('.a-expander-header.a-declarative.a-expander-inline-header.a-link-expander')):
    print("Need help found")
if driver.find_element(By.ID, 'auth-fpp-link-bottom'):
    print("Forgot password link found")
if driver.find_element(By.ID, 'ap-other-signin-issues-link'):
    print("Other issues found")
if driver.find_element(By.ID, 'createAccountSubmit'):
    print("Create account button found")
if driver.find_element(By.LINK_TEXT, 'Conditions of Use'):
    print("Conditions of Use found")
if driver.find_element(By.LINK_TEXT, 'Privacy Notice'):
    print("Privacy Notice found")


driver.quit()
