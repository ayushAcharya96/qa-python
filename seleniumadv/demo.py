from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
driver = webdriver.Chrome(service = service)
driver.get("https://itera-qa.azurewebsites.net/home/automation")

# checkbox = driver.find_element(By.ID, "thursday")
# checkbox.click()

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @class='form-check-input']")

for checkbox in checkboxes:
    checkbox.click()