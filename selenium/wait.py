import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service()
driver = webdriver.Chrome(service=service)
# driver.implicitly_wait(10)
myWait = WebDriverWait(driver,10)
driver.get("https://www.google.com")
driver.find_element(By.NAME, 'q').send_keys("selenium")
driver.find_element(By.NAME, 'q').submit()
# time.sleep(5)
# driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()
# searchlink = myWait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
# searchlink.click()

myWait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']"))).click()
