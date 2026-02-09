import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.neux.com.tw/")
driver.maximize_window()

wait_setting = WebDriverWait(
    driver, timeout=5, ignored_exceptions=Exception)

pop_btn = wait_setting.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[@class='ai-message__close-btn']")))
pop_btn.click()


time.sleep(3)

# scroll by js script in x,y
driver.execute_script("window.scrollBy(0, 300)")
value = driver.execute_script("return window.pageYOffset;")
print(value)
time.sleep(3)


# scroll by js script in element positon
report_btn = wait_setting.until(
    EC.presence_of_element_located((By.LINK_TEXT, "了解我們如何產出洞察報告")))
driver.execute_script(
    "arguments[0].scrollIntoView();", report_btn)
value = driver.execute_script("return window.pageYOffset;")
print(value)


# scroll to end
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
value = driver.execute_script("return window.pageYOffset;")
print(value)
time.sleep(1)

# scroll to init position
driver.execute_script("window.scrollTo(0, 0);")
value = driver.execute_script("return window.pageYOffset;")
print(value)
time.sleep(1)


input("Press Enter to close the browser...")
driver.quit()
