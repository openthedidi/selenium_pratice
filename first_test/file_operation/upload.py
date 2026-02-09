from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("https://formstone.dev/components/upload/demo/")
driver.maximize_window()

time.sleep(2)


upload_btn_list = driver.find_elements(
    By.XPATH, "//div[contains(.,'Drag')]//input[@class='fs-upload-input']")

upload_btn = upload_btn_list[0]
print(upload_btn.tag_name)
upload_btn.send_keys("D:\\selenium-driver\\1213.png")


time.sleep(5)
driver.quit()
