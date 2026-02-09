import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


driver.get(
    "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(2)
driver.get("https://www.google.com")
time.sleep(2)

# ---- 上一頁
driver.back()
time.sleep(2)
# ---- 下一頁
driver.forward()
time.sleep(2)
# ---- 重新整理
driver.refresh()
