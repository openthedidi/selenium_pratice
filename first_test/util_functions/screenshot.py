import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrom_drive = webdriver.Chrome()
chrom_drive.get("https://www.taiwanlife.com/index")

chrom_drive.maximize_window()

wait_setting = WebDriverWait(chrom_drive, 10)

h2_element = wait_setting.until(
    EC.presence_of_element_located((By.XPATH, '//h2[text()="商品快搜"]')))


chrom_drive.save_screenshot("D:\\selenium-driver\\screenshot.png")
chrom_drive.get_screenshot_as_file("D:\\selenium-driver\\screenshot2.png")


chrom_drive.quit()
