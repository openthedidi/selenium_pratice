from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

wait_setting = WebDriverWait(
    driver, timeout=5, ignored_exceptions=Exception)


time.sleep(3)

btn = driver.find_element(
    By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver)
act.context_click(btn).perform()

copy_btn = wait_setting.until(EC.element_to_be_clickable(
    (By.XPATH, "//span[text()='Copy']")))
copy_btn.click()

time.sleep(3)
input("Press Enter to close the browser...")
driver.quit()
