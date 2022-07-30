import os
from pathlib import Path

import selenium.webdriver.ie.service
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://itera-qa.azurewebsites.net/home/automation")

# select all checkbox
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
print(len(checkboxes))
for checkbox in checkboxes:
    week = checkbox.get_attribute("id")
    if week == 'sunday' or week == 'tuesday':
        checkbox.click()

# select checkboxes by choice
