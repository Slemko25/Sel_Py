from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
driver.get("https://www.saucedemo.com")

time.sleep(5)


driver.close()
driver.quit()
