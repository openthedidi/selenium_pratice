from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


chrom_drive = webdriver.Chrome()
chrom_drive.get("https://www.globalsqa.com/demo-site/draganddrop/")

chrom_drive.maximize_window()

wait_setting = WebDriverWait(
    chrom_drive, timeout=5, ignored_exceptions=Exception)


wait_setting.until(EC.frame_to_be_available_and_switch_to_it(
    (By.CSS_SELECTOR, "iframe.demo-frame")))

target_area = wait_setting.until(EC.presence_of_element_located(
    (By.XPATH, "//div[@id='trash']")))

drag_item = wait_setting.until(EC.presence_of_element_located(
    (By.XPATH, "//li//h5[text()='High Tatras']")))


act = ActionChains(chrom_drive)
act.drag_and_drop(drag_item, target_area).perform()

time.sleep(3)


input("Press Enter to close the browser...")
chrom_drive.quit()
