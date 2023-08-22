from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
driver.get("https://magento.softwaretestingboard.com")
driver.maximize_window()
driver.implicitly_wait(2)
driver.refresh()
driver.implicitly_wait(2)

driver.find_element(By.LINK_TEXT, 'Sign In').click()
driver.implicitly_wait(2)

title = driver.title
print(title)
assert title == 'Customer Login'

driver.find_element(By.ID, 'email').send_keys("admin12@gmail.com")
driver.find_element(By.ID, 'pass').send_keys("admin12!@")
driver.implicitly_wait(2)
driver.find_element(By.ID, 'send2').click()

home_page = driver.title

print(home_page)
assert home_page == 'Home Page'
time.sleep(5)

driver.quit()
