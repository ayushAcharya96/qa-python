from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
windowIds = driver.window_handles

parentWindowId = windowIds[0]
childWindowId = windowIds[1]


driver.switch_to.window(childWindowId)
print(driver.title)

driver.switch_to.window(parentWindowId)
print(driver.title)