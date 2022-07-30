# Test cases
# --------------
# 1. Open web browser (chrome/firefox/edge)
# 2. Open URL https://opensource-demo.orangehrmlive.com/
# 3. Enter username (Admin)
# 4. Enter password (admin123)
# 5. Click login
# 6. Capture title of the home page. (Actual title)
# 7. Verify title of the page: OrangeHRM (Expected)
# 8. close browser

from selenium import webdriver

# Selenium 3
# driver = webdriver.Chrome("C:\drivers\chromedriver_win32\chromedriver.exe")
# driver.get("https://opensource-demo.orangehrmlive.com/")
#
# driver.find_element_by_name("txtUsername").send_keys("Admin")
# driver.find_element_by_name("txtPassword").send_keys("admin123")
# driver.find_element_by_id("btnLogin").click()
#
# actual_title = driver.title
# expect_title = "OrangeHRM"
#
# if actual_title == expect_title:
#     print("Login text passed")
# else:
#     print("Login text Failed")
#
# driver.close()


# Selenium 4
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# service_object = Service("C:\drivers\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Firefox()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
# driver.find_element(By.ID, "txtPassword").send_keys("admin123")
# driver.find_element(By.ID, "btnLogin").click()
# actual_title = driver.title
# expect_title = "OrangeHRM"
# if actual_title == expect_title:
#     print("Login test passed")
# else:
#     print("Login test Failed")
# driver.close()

# driver = webdriver.Chrome()
# driver.get("https://admin-demo.nopcommerce.com/login")
# driver.find_element(By.ID, "Email").clear()
# driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
# driver.find_element(By.ID, "Password").clear()
# driver.find_element(By.ID, "Password").send_keys("admin")
# driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
# actual_title = driver.title
# expect_title = "OrangeHRM"
# if actual_title == expect_title:
#     print("Login test passed")
# else:
#     print("Login test Failed")
# driver.close()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")

sliders = driver.find_elements(By.CLASS_NAME, 'homeslider-container')
print(len(sliders))

links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))

driver.close()