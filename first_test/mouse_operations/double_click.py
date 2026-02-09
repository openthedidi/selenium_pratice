from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://www.xbitlabs.com/zh-tw/mouse-double-click-test/")
driver.maximize_window()

wait_setting = WebDriverWait(
    driver, timeout=5, ignored_exceptions=Exception)


time.sleep(3)


double_click_btn = wait_setting.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='text-center']")))

act = ActionChains(driver)
act.double_click(double_click_btn).perform()

time.sleep(3)
input("Press Enter to close the browser...")
driver.quit()
