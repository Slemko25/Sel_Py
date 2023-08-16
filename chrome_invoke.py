from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj = Service("C:\webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.saucedemo.com")

driver.close()
driver.quit()
