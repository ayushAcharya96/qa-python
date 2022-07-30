from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service()
driver = webdriver.Chrome(service=serv)
driver.maximize_window()
driver.get("http://opensource-demo.orangehrmlive.com/")

print(driver.title)
print(driver.current_url)
# print(driver.page_source)
