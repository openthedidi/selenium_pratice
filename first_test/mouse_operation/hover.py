from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


chrom_drive = webdriver.Chrome()
chrom_drive.get("https://www.moneydj.com/etf/")
chrom_drive.maximize_window()

wait_setting = WebDriverWait(
    chrom_drive, timeout=5, ignored_exceptions=Exception)


time.sleep(3)


etf_img_btn = chrom_drive.find_element(
    By.XPATH, "/html/body/div[1]/form/div[2]/div[2]/ul/li[2]/img")

erf_info_btn = chrom_drive.find_element(
    By.XPATH, "//div[@class='bgmenu']//a[text()='基本資料']")

act = ActionChains(chrom_drive)
act.move_to_element(etf_img_btn).move_to_element(
    erf_info_btn).click().perform()


input("Press Enter to close the browser...")
chrom_drive.quit()
