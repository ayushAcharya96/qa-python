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
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()

countries = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")
print(len(countries))
for country in countries:
    if country.text == "Nepal":
        country.click()
