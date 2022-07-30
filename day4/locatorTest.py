import os
from pathlib import Path

import selenium.webdriver.ie.service
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://automationpractice.com/index.php")
driver.get("https://www.google.com")
driver.back()
driver.forward()
driver.refresh()