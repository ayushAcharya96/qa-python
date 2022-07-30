import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

location = os.getcwd()

def chrome_setup():
    service = Service()
    driver = webdriver.Chrome(service= service)
    return driver

driver = chrome_setup()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
# driver.save_screenshot(f"{location}\homepage.png")

# new tab
driver.get("https://www.opencart.com/")
driver.switch_to.new_window('tab')
driver.get("https://www.orangehrm.com/")