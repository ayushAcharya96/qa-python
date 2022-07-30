import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import xlUtils

service = Service()
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-banck-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.implicitly_wait(10)
driver.maximize_window()

file = "D:\\fixeddeposit.xlsx"
sheetName = "Sheet1"
rows = xlUtils.getRowCount(file, sheetName)
print(rows)

for r in range(2, rows):
    # retrieving data from xl
    principal = xlUtils.readData(file, sheetName, r, 1)
    interest = xlUtils.readData(file, sheetName, r, 2)
    period1 = xlUtils.readData(file, sheetName, r, 3)
    period2 = xlUtils.readData(file, sheetName, r, 4)
    frequency = xlUtils.readData(file, sheetName, r, 5)
    exp_mvalue = xlUtils.readData(file, sheetName, r, 6)

    # passing data to the application
    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(int(principal))
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(interest)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(int(period1))
    periodDropDown = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    periodDropDown.select_by_visible_text(period2)
    frequencyDropDown = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    frequencyDropDown.select_by_visible_text(frequency)
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    act_val = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    # validation
    if float(exp_mvalue) == float(act_val):
        print("test passed")
        xlUtils.writeData(file, sheetName, r, 8, "Passed")
        xlUtils.fillGreenColor(file, sheetName, r, 8)
    else:
        print("test failed")
        xlUtils.writeData(file, sheetName, r, 8, "Failed")
        xlUtils.fillRedColor(file, sheetName, r, 8)
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(2)

driver.close()
