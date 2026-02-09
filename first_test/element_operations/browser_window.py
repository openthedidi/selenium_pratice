import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.skbank.com.tw/search")
wait_setting = WebDriverWait(driver, 10)


driver.maximize_window()

time.sleep(3)

# -----by window id in only window
# window_id = driver.current_window_handle
# print(window_id)

# en_btn = driver.find_element(
#     By.XPATH, "//span[@class='header__nav-text ng-tns-c120-0'][normalize-space()='EN']")
# en_btn.click()
# time.sleep(3)
# print(driver.title)
# window_ids = driver.window_handles

# for window_id_list in window_ids:
#     driver.switch_to.window(window_id_list)
#     print(driver.title)
#     time.sleep(1)


# -----另開 tab -----
driver.switch_to.new_window(type_hint='tab')
driver.get("https://www.taiwanlife.com/index")

# -----另開 window -----
driver.switch_to.new_window(type_hint='window')
driver.get("https://www.taiwanlife.com/index")


input("Press Enter to close the browser...")
driver.quit()
