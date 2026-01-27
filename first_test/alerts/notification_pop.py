from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_options = webdriver.ChromeOptions()
# 把像是存取地址的通知關掉
chrome_options.add_argument("--disable-notifications")


chrom_drive = webdriver.Chrome(options=chrome_options)
chrom_drive.get("https://whatmylocation.com")

chrom_drive.maximize_window()

time.sleep(3)


input("Press Enter to close the browser...")
chrom_drive.quit()
