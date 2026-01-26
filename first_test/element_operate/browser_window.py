import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrom_drive = webdriver.Chrome()
chrom_drive.get("https://www.skbank.com.tw/search")


chrom_drive.maximize_window()

time.sleep(3)

# -----by window id in only window
window_id = chrom_drive.current_window_handle
print(window_id)

en_btn = chrom_drive.find_element(
    By.XPATH, "//span[@class='header__nav-text ng-tns-c120-0'][normalize-space()='EN']")
en_btn.click()
time.sleep(3)
print(chrom_drive.title)
window_ids = chrom_drive.window_handles

for window_id_list in window_ids:
    chrom_drive.switch_to.window(window_id_list)
    print(chrom_drive.title)
    time.sleep(1)


input("Press Enter to close the browser...")
chrom_drive.quit()
