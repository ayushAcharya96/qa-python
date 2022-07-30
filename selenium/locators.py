from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://automationpractice.com/index.php")
sliders = driver.find_elements(By.CLASS_NAME, 'homeslider-container')
print(len(sliders))
links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))
# driver.close()

# driver.get("https://www.facebook.com")

# driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys("abc")
# driver.find_element(By.CSS_SELECTOR, 'input#pass').send_keys("abc")
# driver.find_element(By.XPATH,"//*[@id='email']").send_keys("aus.acharya@gmail.com")
# a = driver.find_element(By.XPATH,"//*[@id='email']")
# a.
# driver.find_element(By.XPATH, "//*[@id='pass']").send_keys("sdsfsdf")
# driver.find_element(By.XPATH, '//button[.="Log In"]').click()

