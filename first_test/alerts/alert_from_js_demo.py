import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrom_drive = webdriver.Chrome()
chrom_drive.get("https://the-internet.herokuapp.com/javascript_alerts")

chrom_drive.maximize_window()

time.sleep(3)

btn = chrom_drive.find_element(
    By.XPATH, "//button[text()='Click for JS Prompt']")
btn.click()


alert_window = chrom_drive.switch_to.alert

print(alert_window.text)
# alert_window.send_keys不會出現在window中
alert_window.send_keys("test")

# 只有1個選項時，用accept()即可
alert_window.accept()
# alert_window.dismiss()


input("Press Enter to close the browser...")
chrom_drive.quit()
