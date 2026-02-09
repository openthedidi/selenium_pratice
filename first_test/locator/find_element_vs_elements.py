from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com")
driver.maximize_window()

# ============find_element=============

# find_element return only one element，如果沒有就會噴NoSuchElementException
input_search = driver.find_element(
    By.XPATH, "//input[@id='small-searchterms']")
print(input_search.is_enabled())
input_search.send_keys("20")

time.sleep(5)


# find_element return multi elements，如果沒有就會噴NoSuchElementException
# 只會回傳第一個找到的element

a_href = driver.find_element(
    By.XPATH, "//div[@class='footer-menu']//a")

print(a_href.text)


# =============find_elements=============
a_hrefs = driver.find_elements(
    By.XPATH, "//div[@class='footer-menu']//a")
print(type(a_hrefs))
print(len(a_hrefs))

# 就算找不到也不會噴NoSuchElementException
empty_hrefs = driver.find_elements(
    By.XPATH, "//div[@class='footer-menu']//tr")
print(len(empty_hrefs))
