from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(10)

# login
driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

# admin user management users
admin = driver.find_element(By.XPATH,"//*[@id='menu_admin_viewAdminModule']/b")
usermgmt = driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']")
users = driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']")

# mouse hover
act = ActionChains(driver)

act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()




















# scroll

# driver.execute_script("window.scrollBy(0, 3000)", "")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved", value)

# until visible
# flag = driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']")
# driver.execute_script("arguments[0].scrollIntoView();", flag)

# until end
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

# to initial position
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")

