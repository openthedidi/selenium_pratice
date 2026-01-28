import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


chrom_drive = webdriver.Chrome()
chrom_drive.get("https://www.skbank.com.tw/search")
wait_setting = WebDriverWait(chrom_drive, 10)


chrom_drive.maximize_window()

time.sleep(3)

# -----by window id in only window
# window_id = chrom_drive.current_window_handle
# print(window_id)

# en_btn = chrom_drive.find_element(
#     By.XPATH, "//span[@class='header__nav-text ng-tns-c120-0'][normalize-space()='EN']")
# en_btn.click()
# time.sleep(3)
# print(chrom_drive.title)
# window_ids = chrom_drive.window_handles

# for window_id_list in window_ids:
#     chrom_drive.switch_to.window(window_id_list)
#     print(chrom_drive.title)
#     time.sleep(1)


# -----另開 tab -----
chrom_drive.switch_to.new_window(type_hint='tab')
chrom_drive.get("https://www.taiwanlife.com/index")

# -----另開 window -----
chrom_drive.switch_to.new_window(type_hint='window')
chrom_drive.get("https://www.taiwanlife.com/index")


input("Press Enter to close the browser...")
chrom_drive.quit()
