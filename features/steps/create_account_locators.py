from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://track.amazon.com/register')
time.sleep(2)

if driver.find_element(By.CLASS_NAME, 'a-icon.a-icon-logo'):
    print("Logo found")
if driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small'):
    print("Create account sign found")
if driver.find_element(By.ID, 'ap_customer_name'):
    print("Your name field found")
if driver.find_element(By.ID, 'ap_email'):
    print("Email field found")
if driver.find_element(By.ID, 'ap_password'):
    print("Password field found")
if driver.find_element(By.ID, 'ap_password_check'):
    print("Password validation form found")
if driver.find_element(By.ID, 'continue'):
    print("Registration button found")
if driver.find_element(By.LINK_TEXT, 'Conditions of Use'):
    print("Conditions of Use found")
if driver.find_element(By.LINK_TEXT, 'Privacy Notice'):
    print("Privacy Notice")
if driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis'):
    print("Sign in link found")

driver.quit()