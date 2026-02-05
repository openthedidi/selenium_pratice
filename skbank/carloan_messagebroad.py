from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from config.browser_settings import BrowserSettings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrom_drive = BrowserSettings().get_chrome_driver(maximize=True)
chrom_drive.get(
    "https://www.skbank.com.tw/carloan_messagebroad")

wait_setting = WebDriverWait(chrom_drive, 3)

html_code = chrom_drive.page_source
print(html_code)

input("123")
chrom_drive.quit()
