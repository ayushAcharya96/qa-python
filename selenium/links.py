import os
from pathlib import Path

import selenium.webdriver.ie.service
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")

# driver.find_element(By.LINK_TEXT, "Digital downloadings").click()

links = driver.find_elements(By.TAG_NAME, "a")
print("total number of links", len(links))
for link in links:
    print(link.text)


driver.switch_to.alert.accept()