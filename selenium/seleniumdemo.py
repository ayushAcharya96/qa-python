import os
import time
from pathlib import Path

import selenium.webdriver.ie.service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")
# driver.implicitly_wait(10)
waitBuffer = WebDriverWait(driver, 10)

searchInput = driver.find_element(By.NAME, "q")
searchInput.send_keys("tesla")
searchInput.submit()

teslaResult = waitBuffer.until(EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='Tesla: Electric Cars, Solar & Clean Energy']")))
teslaResult.click()
# driver.find_element/.click()