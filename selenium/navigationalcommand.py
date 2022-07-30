from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service()
driver = webdriver.Chrome(service=serv)
driver.maximize_window()
driver.get("http://www.facebook.com")
driver.get("https://www.amazon.com")

driver.back()
driver.forward()
driver.refresh()

driver.quit()