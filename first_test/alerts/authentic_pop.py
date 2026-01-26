import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrom_drive = webdriver.Chrome()
chrom_drive.get("https://neux:neux1234@proj.walkflow.com.tw/cms/login")

# chrom_drive.get("http://admin:password@the-internet.herokuapp.com/basic_auth")
# Basic Auth 是 HTTP 協定層的機制，
# URL 裡的 username:password@host 會被瀏覽器拿來自動組出 Authorization: Basic ... header
time.sleep(5)

input("Press Enter to close the browser...")
chrom_drive.quit()
