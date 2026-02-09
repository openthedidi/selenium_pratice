import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.maximize_window()

time.sleep(3)

btn = driver.find_element(
    By.XPATH, "//button[text()='Click for JS Prompt']")
btn.click()


alert_window = driver.switch_to.alert

print(alert_window.text)
# alert_window.send_keys不會出現在window中
alert_window.send_keys("test")

# 只有1個選項時，用accept()即可
alert_window.accept()
# alert_window.dismiss()


input("Press Enter to close the browser...")
driver.quit()
