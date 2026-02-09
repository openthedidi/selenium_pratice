import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


driver.get(
    "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

time.sleep(5)

link_href = driver.find_element(
    By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']")
link_href.click()

time.sleep(5)


# -----close()：
# 會關掉driver所代表的分頁(window)，其他從此分頁開啟的不受影響
# driver.close()


# -----quit()：
# 整個browser都會關掉，因為kill drive process了
# driver.quit()
#
