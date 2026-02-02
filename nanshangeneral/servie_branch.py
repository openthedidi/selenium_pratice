from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from config.browser_settings import BrowserSettings


chrom_drive = BrowserSettings().get_chrome_driver(maximize=True)
chrom_drive.get(
    "https://www.nanshangeneral.com.tw/contactus?tabTitle=%E5%8C%97%E5%8D%80&page=1")

wait_setting = WebDriverWait(chrom_drive, 3)


input("123")
chrom_drive.quit()
