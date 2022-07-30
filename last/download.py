import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

location = os.getcwd()

def chrome_setup():
    service = Service()
    preferences = {"download.default_directory" : location }
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(service= service, options=ops)
    return driver

# Automation
driver = chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-downloads/")
driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()


