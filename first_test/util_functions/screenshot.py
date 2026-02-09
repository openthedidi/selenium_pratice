import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.taiwanlife.com/index")

driver.maximize_window()

wait_setting = WebDriverWait(driver, 10)

h2_element = wait_setting.until(
    EC.presence_of_element_located((By.XPATH, '//h2[text()="商品快搜"]')))


driver.save_screenshot("D:\\selenium-driver\\screenshot.png")
driver.get_screenshot_as_file("D:\\selenium-driver\\screenshot2.png")


driver.quit()
