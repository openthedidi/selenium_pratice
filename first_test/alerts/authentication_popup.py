import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://neux:neux1234@proj.walkflow.com.tw/cms/login")

# driver.get("http://admin:password@the-internet.herokuapp.com/basic_auth")
# Basic Auth 是 HTTP 協定層的機制，
# URL 裡的 username:password@host 會被瀏覽器拿來自動組出 Authorization: Basic ... header
time.sleep(5)

input("Press Enter to close the browser...")
driver.quit()
