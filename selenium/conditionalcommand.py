import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service()
driver = webdriver.Chrome(service=serv)
driver.maximize_window()
driver.get("http://demo.nopcommerce.com/register")


time.sleep(5)
driver.close()