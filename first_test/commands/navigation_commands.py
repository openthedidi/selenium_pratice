import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrom_drive = webdriver.Chrome()


chrom_drive.get(
    "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(2)
chrom_drive.get("https://www.google.com")
time.sleep(2)

# ---- 上一頁
chrom_drive.back()
time.sleep(2)
# ---- 下一頁
chrom_drive.forward()
time.sleep(2)
# ---- 重新整理
chrom_drive.refresh()
