from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=serv)
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")

# absolute xpath
# driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[2]/form[1]/input[4]').send_keys("T-shirts")
# driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[2]/form[1]/button[1]').click()

# relative xpath
# driver.find_element(By.XPATH, "//input[@id='search_query_top']").send_keys("T-shirts")
# driver.find_element(By.XPATH, "//button[@name='submit_search']").click()

# or
# driver.find_element(By.XPATH, "//input[@id='search_query_top' or @name='search_query']").send_keys("Tshirts")
# driver.find_element(By.XPATH, "//button[@name='summit_search' and @class='btn btn-default button-search']").click()

# contains
# driver.find_element(By.XPATH,"//input[contains(@id, 'search')]").send_keys("T shirt")
# driver.find_element(By.XPATH, "//button[starts-with(@name, 'submit_')]").click()

# text()
# driver.find_element(By.XPATH, '//a[text()="Women"]').click()
# driver.close()